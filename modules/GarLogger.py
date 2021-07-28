import requests


class GarLogger:
    """Класс логирует и бекапит логи курсов, ставок, лотов"""

    def __init__(self):
        pass

    def first_initial(self):
        """Проверка наличия логов или создание новых"""
        pass

    def beckup(self):
        """резервное копирование логов"""
        pass

    def writer(self):
        """Запись массива данных в логи xml"""


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

if __name__ == '__main__':
    print("Модуль логирования.")
