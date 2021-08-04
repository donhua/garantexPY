import sqlite3 as sql


class Gardb:

    def __init__(self, namedb: str = 'gdb.db'):
        self.namedb = namedb
        self.db = None
        self.sq = ['create table if not exists student(roll_no integer PRIMARY KEY,first_name text,\
                    last_name text, class text, stream text,address text)',]

    def Connectdb(self):
        try:
            self.db = sql.connect(self.namedb)
            print(f"Статус соединения с базой {self.namedb} - УСПЕШНО!")
        except sql.Error:
            print(sql.Error)
        finally:
            print('ok')

    def Create_table(self):
        cursor_object = self.db.cursor()
        cursor_object.execute(self.sq[0])
        self.db.commit()
        print('yes')
        self.db.close()

    def Deletedb(self):
        pass

def mee():
    n = Gardb()
    n.Connectdb()
    n.Create_table()


if __name__ == '__main__':
    mee()


