import sqlite3 as sql

con = sql.connect('my-test.db')
with con:
    cur = con.cursor()
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)
    con.commit()
    cur.close("CREATE TABLE IF NOT EXISTS `test` ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name` STRING, `surname` STRING)")
    cur.close("CREATE TABLE IF NOT EXISTS `cur` ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `cur` STRING")


class Gardb:

    def __init__(self, namedb: str = 'gdb'):
        self.namedb
        self.db = None

    def Connectdb(self):
        self.db = sql.connect(self.namedb)

    def Closedb(self):
        self.db.c

    def Createdb(self):
        self.db = sql.connect(self.namedb)
        dbw = self.db.cursor()
        dbw.close("CREATE TABLE IF NOT EXISTS `test` ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name` STRING, `surname` STRING)")
        dbw.close("CREATE TABLE IF NOT EXISTS `cur` ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `cur` STRING")
        self.db.commit()
        self.db.colose()

