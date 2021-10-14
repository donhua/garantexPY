#!/usr/bin/env python3

from gar_modul.GarantexIo import GarantexIo as GI

def zero(o : int, l : list, i: int, j : int):
    """Принимает максимальную длину строки, список и номер элемента списка.
    возвращает строку с дописанными символами в конце строки до максимальной длины"""
    o1 = o - len(l[i][j])
    if o1 < 0:
        o1 = 0
    return l[i][j]+'0'*o1

gi = GI()
a = gi.get_history_market('btcrub')
print(len(a))
for i in a:
    l = list(i.items())
    ll = l[1:5]
    t1 = zero(10, ll, 0, 1)
    t2 = zero(10, ll, 1, 1)
    t = f'Курс {t1} | {t2} btc |'
