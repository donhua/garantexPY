#!/usr/bin/env python3
import sqlite3 as sql
from pathlib import Path
import datetime
import logging
from sqlite3 import Connection


class Gardb:

    def __init__(self):
        self.lg = logging
        '''self.lg.basicConfig(filename=self.pathlog,
                            level=logging.INFO,
                            format='%(asctime)s-%(levelname)s-%(message)s')'''
        self.db_file = 'gdb.db'
        self.db_file_backup: str = "backup.db"
        self.db_file_log: str = 'db.log'
        self.db_dir = 'db'
        self.db_dir_backup = 'backup'
        self.db_dir_log = 'log'
        self.sq_table = [
            '''CREATE TABLE IF NOT EXISTS curensy(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    kur TEXT(5)
                    );''',
            '''CREATE TABLE IF NOT EXISTS curensy_type(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    type TEXT(5)
                    );''',
            '''CREATE TABLE IF NOT EXISTS lot(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    lot_Date TIMESTAMP,
                    lot_fiat REAL,
                    lot_coin REAL,
                    coin_type INT,
                    exchange REAL
                    );''',
            '''CREATE TABLE IF NOT EXISTS kash(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    kash_Date TIMESTAMP,
                    kash_fiat REAL
                    );''',
        ]
        self.db = None
        self.backup_con = None
    def create_tath(self):
        if path.is_dir(self.pathlog):
            path.rmdir(self.pathlog)
            

    def connect_db(self):
        try:
            self.db: Connection = sql.connect(self.db_path+self.name_db)
            self.lg.info(f"Статус соединения с базой {self.name_db} - УСПЕШНО!")
            with self.db:
                cursor_object = self.db.cursor()
                for i in self.sq_table:
                    cursor_object.execute(i)
                    self.lg.info(f'Создание таблицы {self.table_name[0]} - успешно!')
                self.db.commit()
        except sql.Error:
            self.lg.error(sql.Error)
        finally:
            self.db.close()
            self.lg.info(f'Закрытие базы {self.name_db} - успешно!')

    def gar_backup(self, path: str = './backup/'):
        try:
            t = datetime.datetime.now()
            self.db = sql.connect(Path(self.db_path+self.name_db))
            self.backup_db_name = str(t) + "_" + self.name_db[:(len(self.name_db) - 3)] + '_backup.db'
            self.backup_con: Connection = sql.connectPath(Path(path + self.backup_db_name))
            with self.backup_con:
                self.db.backup(self.backup_con, pages=3, progress=None)
            self.lg.info(f"Бекап {self.name_db} - успешно!")
        except sql.Error as error:
            self.lg.error(f"Ошибка бекапа {self.name_db}: " + str(error))
        finally:
            if self.backup_con:
                self.backup_con.close()
                self.db.close()
                self.lg.info(f'Закрытие базы {self.name_db} и {self.backup_db_name}- успешно!')

    def get_tables(self):
        try:
            self.db = sql.connect(self.db_path+self.name_db)
            cur = self.db.cursor()
            self.lg.info(f"Статус соединения с базой {self.name_db} - УСПЕШНО!")
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            return cur.fetchall()
        except sql.Error:
            self.lg.error(sql.Error)
        finally:
            self.db.close()
            self.lg.info(f'Закрытие базы {self.name_db} - успешно!')

    def lot_table(self, data: list, i: int):
        try:
            self.db: Connection = sql.connect(self.db_path + self.name_db)
            self.lg.info(f"Статус соединения с базой {self.name_db} - УСПЕШНО!")
            with self.db:
                cursor_object = self.db.cursor()
                cursor = cursor_object.execute(f'select * from {self.table_name[i]}')
                arr = []
                for row in cursor.description:
                    arr.append(row[0])
                row_table = ', '.join(arr[1:])
                print(f"INSERT INTO {self.table_name[i]} ({row_table}) VALUES ({','.join('?'*len(data))})")
                cursor_object.execute(f"INSERT INTO {self.table_name[i]} ({row_table}) VALUES ({','.join('?'*len(data))})", data)
                self.db.commit()
                self.lg.info(f'Запись в таблицу {self.table_name[i]} - успешно!')
        except sql.Error:
            self.lg.error(sql.Error)
        finally:
            self.db.close()
            self.lg.info(f'Закрытие базы {self.name_db} - успешно!')

def mee():
    n = Gardb()
    n.create_tath()


if __name__ == '__main__':
    mee()
