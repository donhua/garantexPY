#!/usr/bin/env python3
# pyinstaller --onefile main.py

from decimal import Decimal, ROUND_FLOOR

# pip install requests
import requests


class DealInf:
    """Класс для работы с файлом ставок"""

    def __init__(self, path: str = 'deal.inf'):
        self.path = path
        self.dealslist = []

    def verififiles(self):
        """Проверяет наличие файла deal.inf если отсуьсьвует, то создает и предлагает заполнить его"""
        try:
            f = open(self.path)
            f.close()
            print('File found. Ok.')
            print('!!!После изменения файла перезапустите программу!!!')
        except FileNotFoundError:
            print('Файл не существовал, но теперь создан. Заполните его данными: сумма, курс, комиссия, Id маркета')
            f = open(self.path, "w")
            f.close()
            input()
            exit()

    def readfiles(self, market):
        """Принимает ID маркета. возвращаеи массив по всем текущим сделками по текущему рынку"""
        self.dealslist.clear()
        with open(self.path, 'r') as f:
            for i in f:
                ilist = i.split(' ')
                if market in ilist:
                    self.dealslist.append(ilist[:3])
        return self.dealslist


class CalculateFin:
    """Финансовый калькулятор"""

    def signalprofit(self, market, nowcur) -> float:
        """Принимает массив массивов [сумма, курс, налог] по всем ставками маркета.
        возвращает разницу по текущему курсу в рублях"""
        delta = float(self.mycoin(market)) * float(nowcur) * 0.9995 - float(self.marketinvest(market))
        return delta

    def signalitem(self, i: list, nowcur) -> float:
        """Принимает массив массивов [сумма, курс, налог] по всем ставками маркета
        возвращает профит по каждой позиции"""
        profitin = (float(i[0]) / float(i[1])) * float(nowcur) * 0.9995 - float(i[0])
        return profitin

    def mycoin(self, market: list) -> float:
        """Принимает массив массивов [сумма, курс, налог] по всем ставками маркета
        возвращает сумму крипты по маткету"""
        coin = 0
        for i in market:
            coin += float(i[0]) / float(i[1])
        return coin

    def marketinvest(self, market: list) -> float:
        """Принимает массив массивов [сумма, курс, налог] по всем ставками маркета
        возвращает сумму инвестиций по маткету"""
        money = 0
        for i in market:
            money += float(i[0])
        return money

    def deltacur(self, market: list) -> float:
        """Принимает массив массивов [сумма, курс, налог] по всем ставкам маркета
        возвращает общий средний курс инвестиции"""
        coin = self.mycoin(market)
        mymoney = self.marketinvest(market)
        return mymoney / coin

    def totalinvest(self, btn: float, eth: float, dai: float) -> float:
        """Принимает сумму инвестиций по каждому маркету. Возвращает сумму инвестиций по всем маркетам"""
        suminvest = btn + eth + dai
        return suminvest

    def percentprofit(self, suminvest: float, delta: float) -> float:
        """возвращает процент профита или дефицита от вложенной суммs"""
        percent = (100 * (suminvest + delta) / suminvest)
        return percent


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


def dec_over(a: float, masck: str = '1.00'):
    """обрезает цифру для правильного отображения"""
    b = Decimal(a)
    return b.quantize(Decimal(masck), ROUND_FLOOR)


MARKETS = ['btcrub', 'ethrub', 'dairub']
# pyinstaller --onefile main.py


def profitflag(a):
    if a > 0:
        return '***Profit***'
    return 'No profit'


def main(MARKETS):
    calc = CalculateFin()
    deals = DealInf()
    deals.verififiles()

    for i in MARKETS:
        dealslist = deals.readfiles(i)
        lot = GarantexIo(i)
        lot.requeststack()
        ask = lot.requestask()
        bid = lot.requestbid()
        print('--------------------' + i[:3] + '----------------------')
        print('<<<<<<<<<<', i, ask, bid)
        if len(dealslist) != 0:
            ask = lot.requestask()
            signal = calc.signalprofit(dealslist, ask)
            for item in dealslist:
                str_item = ' '.join(item[:2])
                p = dec_over(calc.signalitem(item, ask))
                print(i, str_item, profitflag(p), p)
            print('------------------TOTAL-' + i[:3] + '------------------')
            print(profitflag(dec_over(signal)), i, '>>>>>>>>>>', dec_over(signal))
    text = input("Enter для продолжения!")
    if text == '':
        main(MARKETS)
    exit()


if __name__ == '__main__':
    main(MARKETS)
