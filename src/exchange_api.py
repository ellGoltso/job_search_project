import json
import os

import requests
from dotenv import load_dotenv


class ExchangeAPI:
    """Класс для получения курсов валют"""

    __slots__ = "__apikey"

    def __init__(self):
        load_dotenv()
        self.__apikey = os.getenv("APIKEY_EXCHANGE")

    def exchange_rate(self, filename: str = "data/exchange_rate.json"):
        """Отправляет api запрос и сохраняет ответ в json файл"""

        currencies = "GBP,JPY,EUR,UZS,USD,AZN,KZT,KGS,BYN"
        source = "RUB"
        url = f"https://api.apilayer.com/currency_data/live?source={source}&currencies={currencies}"
        headers = {"apikey": self.__apikey}

        response = requests.request("GET", url, headers=headers)

        if response.status_code != 200:
            print(f"Не удалось получить данные о курсах валют\n{response.status_code}")
            return None

        response = response.json()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(response, f, indent=4, ensure_ascii=False)
