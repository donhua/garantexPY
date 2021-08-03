import sqlite3 as sql


class Gardb:

    def __init__(self, namedb: str = 'gdb'):
        self.namedb = namedb
        self.db = None

    def Connectdb(self):
        self.db = sql.connect(self.namedb)


    def Createdb(self):
        self.db = sql.connect(self.namedb)
        with self.db:
            dbw = self.db.cursor()
            dbw.execute("CREATE TABLE IF NOT EXISTS `test` ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name` STRING, `surname` STRING)")
            dbw.execute("CREATE TABLE IF NOT EXISTS `curi` ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `cur` STRING)")
            dbw.execute("SELECT name FROM sqlite_master WHERE type='table';")
            print(dbw.fetchall())
            self.db.commit()


    def Deletedb(self):
        self.db = sql.connect(self.namedb)
        dbw = self.db.cursor()
        pass

def mee():
    n = Gardb()
    n.Createdb()


if __name__ == '__main__':
    mee()


