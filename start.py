from gar_modul.GarBotTele import GarBotTele
from gar_modul.Gardb import Gardb


dervish: str = '1945392418:AAGWcxG4QHLx0c0uFVVRc0oDdL1VU6WCr64'
dervish_bot = GarBotTele(dervish)
f = Gardb()
dervish_bot.send_message(f.get_tables())
#s = gar_modul.GarBotTele('1945392418:AAGWcxG4QHLx0c0uFVVRc0oDdL1VU6WCr64')
#s.GarBotTele.send_message(f.Gardb.Get_Tables())

