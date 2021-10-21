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
a = gi.requeststack()
b = round(float(a['asks'][0]['price'])-float(a['bids'][0]['price']), 2)
per = round(b*100/float(a['bids'][0]['price']), 2)
print(f"Дельта: {b}")
print(f'{per}%')