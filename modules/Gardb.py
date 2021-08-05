import sqlite3 as sql
import datetime
import logging


class Gardb:

    def __init__(self, namedb1: str = 'gdb.db'):
        self.namedb = namedb1
        self.db = None
        self.table_name = ['curensy', 'curensy_type', 'lot', 'kash']
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
                            filename='../log/app.log',
                            level=logging.INFO,
                            format='%(asctime)s-%(levelname)s-%(message)s',
                            )

    def Connectdb(self):
        try:
            self.db = sql.connect(self.namedb)
            logging.info(f"Статус соединения с базой {self.namedb} - УСПЕШНО!")
            for i in self.sq:
                self.Create_table(i, self.db.cursor())
            self.db.commit()
        except sql.Error:
            logging.error(sql.Error)
        finally:
            self.db.close()
            logging.info(f'Закрытие базы {self.namedb} - успешно!')

    def Create_table(self, sql_request, cursor_object):
        cursor_object.execute(sql_request)
        logging.info(f'Создание таблицы {self.table_name[0]} - успешно!')

    def Deletedb(self):
        pass

    def Gar_backup(self):
        try:
            t = datetime.datetime.now()
            self.db = sql.connect(self.namedb)
            backup_db_name = str(t) +"_" + self.namedb[:(len(self.namedb)-3)] + '_backup.db'
            backup_con = sql.connect('../backup/'+backup_db_name)
            with backup_con:
                self.db.backup(backup_con, pages=3, progress=None)
            logging.info(f"Бекап {self.namedb} - успешно!")
        except sql.Error as error:
            logging.error(f"Ошибка бекапа {self.namedb}: " + str(error))
        finally:
            if backup_con:
                backup_con.close()
                self.db.close()
                logging.info(f'Закрытие базы {self.namedb} и {backup_db_name}- успешно!')


def mee():
    n = Gardb()
    n.Connectdb()
    n.Gar_backup()


if __name__ == '__main__':
    mee()


