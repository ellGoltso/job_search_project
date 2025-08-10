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
    #
    # @abstractmethod
    # def delete_data(self):
    #     pass


class JSONSaver(BaseSaver):

    def __init__(self, filename = "data/vacancies.json"):
        self.filename = filename

    def get_data(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    def add_data(self, vacancies_list: list[Vacancy]):
        vacancies_list_dict = []
        for vacancy in vacancies_list:
            vacancies_list_dict.append(vacancy.to_dict())
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(vacancies_list_dict, f, indent=4, ensure_ascii=False)