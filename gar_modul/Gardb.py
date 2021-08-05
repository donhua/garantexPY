#!/usr/bin/env python3
import sqlite3 as sql
import datetime
import logging
from sqlite3 import Connection


class Gardb:

    def __init__(self, name_db1: str = 'gdb.db'):
        self.name_db = name_db1
        self.db = None
        self.backup_db_name: str = "backup.db"
        self.backup_con = None
        self.table_name: list = ['curensy', 'curensy_type', 'lot', 'kash']
        self.sq = [
            f'''CREATE TABLE IF NOT EXISTS {self.table_name[0]}(
                    id INT PRIMARY KEY,
                    kur TEXT(5)
                    );''',
            f'''CREATE TABLE IF NOT EXISTS {self.table_name[1]}(
                    id INT PRIMARY KEY,
                    type TEXT(5)
                    );''',
            f'''CREATE TABLE IF NOT EXISTS {self.table_name[2]}(
                    id INT PRIMARY KEY,
                    lot_Date TIMESTAMP,
                    lot_fiat REAL,
                    lot_coin REAL,
                    coin_type INT,
                    exchange real
                    );''',
            f'''CREATE TABLE IF NOT EXISTS {self.table_name[3]}(
                    id INT PRIMARY KEY,
                    kash_Date TIMESTAMP,
                    kash_fiat REAL
                    );''',
        ]
        logging.basicConfig(
            filename='../logger/app.log',
            level=logging.INFO,
            format='%(asctime)s-%(levelname)s-%(message)s',
        )

    def connect_db(self):
        try:
            self.db = sql.connect(self.name_db)
            logging.info(f"Статус соединения с базой {self.name_db} - УСПЕШНО!")
            for i in self.sq:
                self.create_table(i, self.db.cursor())
            self.db.commit()
        except sql.Error:
            logging.error(sql.Error)
        finally:
            self.db.close()
            logging.info(f'Закрытие базы {self.name_db} - успешно!')

    def create_table(self, sql_request, cursor_object):
        cursor_object.execute(sql_request)
        logging.info(f'Создание таблицы {self.table_name[0]} - успешно!')

    def delete_db(self):
        pass

    def gar_backup(self):
        try:
            t = datetime.datetime.now()
            self.db = sql.connect(self.name_db)
            self.backup_db_name = str(t) + "_" + self.name_db[:(len(self.name_db) - 3)] + '_backup.db'
            self.backup_con: Connection = sql.connect('../backup/' + self.backup_db_name)
            with self.backup_con:
                self.db.backup(self.backup_con, pages=3, progress=None)
            logging.info(f"Бекап {self.name_db} - успешно!")
        except sql.Error as error:
            logging.error(f"Ошибка бекапа {self.name_db}: " + str(error))
        finally:
            if self.backup_con:
                self.backup_con.close()
                self.db.close()
                logging.info(f'Закрытие базы {self.name_db} и {self.backup_db_name}- успешно!')

    def get_tables(self):
        try:
            self.db = sql.connect(self.name_db)
            cur = self.db.cursor()
            logging.info(f"Статус соединения с базой {self.name_db} - УСПЕШНО!")
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            return cur.fetchall()
        except sql.Error:
            logging.error(sql.Error)
        finally:
            self.db.close()
            logging.info(f'Закрытие базы {self.name_db} - успешно!')


def mee():
    n = Gardb()
    n.connect_db()
    n.gar_backup()


if __name__ == '__main__':
    mee()
