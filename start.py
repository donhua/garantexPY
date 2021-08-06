from gar_modul.GarBotTele import GarBotTele
from gar_modul.Gardb import Gardb
from gar_modul.GarantexIo import GarantexIo
from gar_modul.GarantexIo import GarantexIo22222
import datetime
import os
import requests


g = GarantexIo()
s = g.get_markets()
print(s)
print(os.uname())

'''dervish: str = '_'
b = Gardb()
b.connect_db()
data = [str(datetime.datetime.now()), 2000.20, 0.000023123, 1, 2345675]
b.lot_table(data, 2)'''
