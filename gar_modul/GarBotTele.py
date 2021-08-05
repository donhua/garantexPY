#!/usr/bin/env python3
import requests


class GarBotTele:
    """телеграмм бот для торговли"""

    def __init__(self, token: str):
        self.offset = 0
        self.token = token
        self.url = 'https://api.telegram.org/bot'+self.token+'/'
        self.data = {'offset': self.offset, 'limit': 0, 'timeout': 0}

    def verefi(self):
        """проверка доступности телеги"""
        pass

    def get_me(self):
        return requests.get(self.url+'getMe').json()['ok']

    def get_updates(self):
        return requests.get(self.url+'getUpdates', data=self.data).json()

    def send_message(self, text1: str = "?"):
        send = {'chat_id': 681628513, 'text': text1}
        requests.get(self.url+'sendMessage', data=send)


def mee():
    me = GarBotTele('1945392418:AAGWcxG4QHLx0c0uFVVRc0oDdL1VU6WCr64')
    me.send_message("Xnj 'nj nfrjt!!!!!")


if __name__ == '__main__':
    mee()
