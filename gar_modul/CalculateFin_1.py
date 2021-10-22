#!/usr/bin/env python3
from statistics import mean

class CalculateFin1_1:
    """Финансовый калькулятор"""

    def sum_invests(arr_invests: list = []):
        '''принимает список инвестиций, возвращает сумму'''
        return sum(arr_invests)

    def mean_kurs(arr_kurs):
        '''принимает список значений, возвращает среднее'''
        return round(mean(arr_kurs), 2)

    def signal_seil(kurs_in_time, kurs_meam, persent_marga):
        delta = kurs_in_time-kurs_meam
        persent_in_time = round(delta * 100 / kurs_meam, 2)
        if persent_in_time >= persent_marga:
            return ['', persent_in_time]
        else:
            return [persent_in_time, '']
