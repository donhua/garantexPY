import requests

class GarBotTele:
    """телеграмм бот для торговли"""

    def __init__(self, token: str):
        self.offset = 0
        self.token = token
        self.url = 'https://api.telegram.org/bot'+self.token+'/'
        self.data = {'offset': self.offset, 'limit': 0, 'timeout': 0}


    def verefic(self):
        """проверка доступности телеги"""
        pass

    def getMe(self):
        request = requests.get(self.url+'Message')
        get_Me = request.json()['ok']
        return get_Me

    def get_updates(self):
        result = requests.get(self.url+'getUpdates', data=self.data).json()
        return result

    def send_message(self, text1: str = "?"):
        send = {'chat_id': 681628513, 'text': text1}
        requests.get(self.url+'sendMessage', data=send)


def mee():
    me = GarBotTele('1945392418:AAGWcxG4QHLx0c0uFVVRc0oDdL1VU6WCr64')
    i = 1
    while i == 1:
        t = input('Введи текст: ')
        me.send_message(t)


if __name__ == '__main__':
    mee()
