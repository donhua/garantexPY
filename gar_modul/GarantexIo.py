#!/usr/bin/env python3
import requests


class GarantexIo:
    """Методы API Guarantee.io"""

    def __init__(self, url: str = 'https://garantex.io/api/v2/'):
        self.url = url
        self.url_node = ['markets',
                         'currencies',
                         'timestamp',
                         'fees/withdraw/coin',
                         'trades']

    def get_markets(self):
        """Запрос возвращает список всех активных рынков"""
        try:
            return requests.get(self.url+self.url_node[0]).json()
        except:
            return "!Ошибка запроса списка активных рынков!"

    def get_currencies_type(self, type_curr: str = ''):
        """Запрос для получения списка криптовалют/фиат доступных для работы."""
        type_currencies = ['coin', 'fiat']
        if type_curr in type_currencies:
            par = dict(type=type_curr)
            return requests.get(self.url + self.url_node[1], params=par).json()  
            '''!!!!!!!!!ошибки!!!!!!!!!!!!'''
        else:
            for i in type_currencies:
                par = dict(type=i)
                return requests.get(self.url + self.url_node[1], params=par).json()

    def time_stamp(self):
        """Запрос возвращает текущее время сервера"""
        url = f"{self.url}{self.url_node[2]}"
        return requests.get(url).json()

    def get_fee_coin(self):
        """Запрос возвращает акутальные комиссии на вывод крипты"""
        url = f"{self.url}{self.url_node[3]}"
        return requests.get(url).json()

    def get_gateway_types(self):
        """Запрос возвращает список всех активных направлений ввода / вывода для фиата"""
        pass

    def get_history_market(self, i : str):
        """Запрос возвращает историю сделок по выбранному рынку. i ринимае значения вида btcrub"""
        mr = dict(market = i)
        return requests.get(self.url + self.url_node[4], params = mr).json()

    def get_trades(self, market_, ):
        pass


class GarantexIo22222:
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
