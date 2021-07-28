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