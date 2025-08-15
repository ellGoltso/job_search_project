import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class BaseSaver(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def add_data(self, vacancies_list):
        pass

    @abstractmethod
    def delete_data(self, target):
        pass


class JSONSaver(BaseSaver):

    def __init__(self, filename: str = "data/vacancies.json"):
        self.__filename = filename

    def get_data(self):
        """Возвращает список словарей с вакансиями из json файла"""

        with open(self.__filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []
            return data

    def add_data(self, vacancies_list: list[Vacancy]):
        """Принимает список вакансий list[Vacancy], проверяет вакансии на повтор и сохраняет уникальные в файл json"""

        vacancies_list_dict = self.get_data()
        for vacancy in vacancies_list:
            vacancy_dict = vacancy.to_dict()
            if not self.__is_dict_in_list(vacancy_dict, vacancies_list_dict):
                vacancies_list_dict.append(vacancy_dict)

        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(vacancies_list_dict, f, indent=4, ensure_ascii=False)

    def delete_data(self, target: Vacancy):
        """Принимает одну вакансию, если она сохранена в файле, удаляет ее оттуда"""

        data = self.get_data()
        target_dict = target.to_dict()
        if self.__is_dict_in_list(target_dict, data):
            data.remove(target_dict)
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def __is_dict_in_list(target: dict, list_dict: list[dict]) -> bool:
        """Проверяет наличие словаря в списке словарей, возвращает bool"""

        for dictionary in list_dict:
            if dictionary == target:
                return True
        return False
