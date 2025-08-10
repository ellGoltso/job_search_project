from abc import ABC, abstractmethod
import requests
import os
import json
from dotenv import load_dotenv


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
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []


    def __connect_api(self, keyword):
        self.__params['text'] = keyword
        while self.__params['page'] != 5:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code != 200:
                raise requests.exceptions.RequestException(f"Ошибка! Запрос не выполнен. Статус: {response.status_code}")
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
        return self.__vacancies


    def get_vacancies(self, keyword):
        self.__connect_api(keyword)
        return self.__vacancies


class ExchangeAPI:
    """Класс для получения курсов валют"""

    __slots__ = '__apikey'

    def __init__(self):
        load_dotenv()
        self.__apikey = os.getenv('APIKEY_EXCHANGE')

    def exchange_rate(self):

        currencies = "GBP,JPY,EUR,UZS,USD,AZN,KZT,KGS,BYN"
        source = "RUB"
        url = f"https://api.apilayer.com/currency_data/live?source={source}&currencies={currencies}"
        headers = {
            "apikey": self.__apikey
        }

        response = requests.request("GET", url, headers=headers)

        if response.status_code != 200:
            print(f"Не удалось получить данные о курсах валют\n{response.status_code}")
            return None

        response = response.json()
        with open("data/exchange_rate.json", "w", encoding="utf-8") as f:
            json.dump(response, f, indent=4, ensure_ascii=False)
