from abc import ABC, abstractmethod

import requests


class BaseApi(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(BaseApi):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def __connect_api(self, keyword):
        """Отправляет api запрос hh.ru и сохраняет ответ в свойстве __vacancies"""

        self.__params["text"] = keyword
        while self.__params["page"] != 5:
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )
            if response.status_code != 200:
                raise requests.exceptions.RequestException(
                    f"Ошибка! Запрос не выполнен. Статус: {response.status_code}"
                )
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    def get_vacancies(self, keyword):
        """Вызывает приватный метод __connect_api и возвращает вакансии"""

        self.__connect_api(keyword)
        return self.__vacancies
