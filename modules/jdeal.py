import json


class Jdeal:
    def __init__(self, jpath: str = "deal.json"):
        self.path = jpath
        self.data = None

    def verificfile(self):
        try:
            with open('test.txt', 'r') as f:
                print("File is OK!")
                self.data = json.load(f)
        except FileNotFoundError:
            data = {"btnrub" : [], "ethrub" : [], "dairub" : []}
            with open('test.txt', 'w') as f:
                json.dump(data, f)
                print("Файл создан. Заполните его данными!")

    def getjdata(self):
        return self.data

