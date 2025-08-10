import json


class Vacancy:
    __slots__ = (
        "name",
        "salary",
        "link_to_vacancy",
        "requirement",
        "currency",
        "responsibility",
    )

    def __init__(
        self, name, salary, currency, link_to_vacancy, requirement, responsibility
    ):
        self.name = name
        self.salary = int(salary)
        self.currency = currency
        self.link_to_vacancy = link_to_vacancy
        self.requirement = requirement
        self.responsibility = responsibility

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        raise TypeError("Неверный тип данных")

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        raise TypeError("Неверный тип данных")

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        raise TypeError("Неверный тип данных")

    def __repr__(self):
        return (
            f'\n"name": {self.name}\n"salary": {self.salary} {self.currency}\n'
            f'"link_to_vacancy": {self.link_to_vacancy}\n'
            f'"requirement": {self.requirement}\n"responsibility": {self.responsibility}\n'
        )

    @property
    def get_responsibility(self):
        return self.responsibility

    @classmethod
    def cast_to_object_list(cls, hh_vacancies: list[dict]) -> list:
        vacancies_list = []
        for vacancy in hh_vacancies:
            name = vacancy["name"]
            currency = ""
            if vacancy["salary"] is None:
                salary = 0
            else:
                salary = cls.__salary_validation(vacancy["salary"])
                currency = "RUB"

            alternate_url = vacancy["alternate_url"]
            requirement = vacancy["snippet"]["requirement"]
            responsibility = vacancy["snippet"]["responsibility"]
            vacancies_list.append(
                cls(name, salary, currency, alternate_url, requirement, responsibility)
            )
        return vacancies_list

    @classmethod
    def cast_to_obj_from_file(cls, vacancies: list[dict]) -> list:
        vacancies_list = []
        for vacancy in vacancies:
            vacancies_list.append(cls(**vacancy))
        return vacancies_list

    @staticmethod
    def __salary_validation(salary_range: dict) -> int:

        if salary_range["from"] is not None and salary_range["to"] is not None:
            average_salary = int((salary_range["from"] + salary_range["to"]) / 2)
        elif salary_range["from"] is not None:
            average_salary = salary_range["from"]
        else:
            average_salary = salary_range["to"]

        with open("data/exchange_rate.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        rates = data["quotes"]
        symbols_list = ["GBP", "JPY", "EUR", "UZS", "USD", "AZN", "KZT", "KGS"]

        if salary_range["currency"] == "RUR" or salary_range["currency"] == "RUB":
            return average_salary
        elif salary_range["currency"] in symbols_list:
            average_salary = average_salary / rates["RUB" + salary_range["currency"]]
        elif salary_range["currency"] == "BYR":
            average_salary = average_salary / rates["RUBBYN"]

        return int(average_salary)

    def to_dict(self):
        return {
            "name": self.name,
            "salary": self.salary,
            "currency": self.currency,
            "link_to_vacancy": self.link_to_vacancy,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }
