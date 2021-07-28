

class GarantexIo:
    """Методы API Garantex.io"""

    def __init__(self):
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
