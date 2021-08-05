from gar_modul.GarBotTele import GarBotTele
from gar_modul.Gardb import Gardb
import datetime

dervish: str = '_'
b = Gardb()
b.connect_db()
data = [str(datetime.datetime.now()), 2000.20, 0.000023123, 1, 2345675]
b.lot_table(data, 2)
