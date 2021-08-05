#!/usr/bin/env python3
import requests


class GarantexIo1:
    """Методы API Garantex.io"""

    def __init__(self, url: str = 'https://garantex.io/api/v2/'):
        self.url = url
        self.url_node = ['markets',
                         'currencies',
                         'timestamps',
                         'fees/withdraw/coin',]
        self.markets = []
        self.currencies = []
        self.timestamps = ''
        self.fee_coin = []

    def verefic(self):
        """проверка доступности сайта"""
        pass

    def Get_markets(self):
        """Запрос возвращает список всех активных рынков"""
        response_markets = requests.get(self.url+self.url_node[0])
        self.markets = response_markets.json()

    def Get_currencies_type(self, type_curr: str = ''):
        """Запрос для получения списка криптовалют/фиат доступных для работы."""
        type_currencies = ['coin', 'fiat']
        if type_curr in type_currencies:
            response_currencies = requests.get(self.url + self.url_node[1], params=type_curr)
            self.currencies.append(response_currencies.json())
        else:
            for i in type_currencies:
                response_currencies = requests.get(self.url + self.url_node[1], params=i)
                self.currencies.append(response_currencies.json())

    def Time_stamp(self):
        """Запрос возвращает текущее время сервера"""
        response_timestamps = requests.get(self.url + self.url_node[3])
        self.timestamps = response_timestamps.json()

    def Get_fee_coin(self):
        """Запрос возвращает акутальные комиссии на вывод крипты"""
        response_fee_coin = requests.get(self.url + self.url_node[3])
        self.fee_coin = response_fee_coin.json()

    def Get_gateway_types(self):
        """Запрос возвращает список всех активных направлений ввода / вывода для фиата"""
        pass

    def Get_trades(self, market_, ):
        pass





class GarantexIo:
    """Класс обрабатывает запросы с сайта garantex.io"""

    def __init__(self, marketid: str = 'btcrub', adress_api: str = "https://garantex.io/api/v2/depth"):
        """часть адреса API для Garantex.io"""
        self.adress = adress_api
        self.market = dict(market=marketid)
        self.kurs_full = []

    def verefic(self):
        """проверка доступности сайта"""
        pass

    def requeststack(self):
        """Получаем массив цен стакан"""
        response_kurs = requests.get('https://garantex.io/api/v2/depth', params=self.market)
        self.kurs_full = response_kurs.json()

    def requestask(self):
        """Получаем массив цен стакана продажи"""
        kurs_asks = self.kurs_full.get('asks')
        kurs_asks_first = kurs_asks[0]
        kurs_asks_first_price = kurs_asks_first.get('price')
        return kurs_asks_first_price

    def requestbid(self):
        """Получаем массив цен стакана покупки"""
        kurs_asks = self.kurs_full.get('bids')
        kurs_asks_first = kurs_asks[0]
        kurs_asks_first_price = kurs_asks_first.get('price')
        return kurs_asks_first_price

    def requestmarkets(self):
        """Получаем массив маркетов"""
        response_kurs = requests.get('https://garantex.io/api/v2/markets')
        markets_full = response_kurs.json()
        return markets_full
