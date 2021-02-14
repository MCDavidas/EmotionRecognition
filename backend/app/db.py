import os
import sys
import logging
import mysql.connector as mariadb


DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')


class DBManager:
    def __init__(self, database='ERProject',
                 host="localhost", port=3306, user="root",
                 password_file=os.path.join(DATA_PATH, 'mariadb-pw.txt')):
        logging.info(f'Connecting to mariadb {host}, {port}, {database}')
        pf = open(password_file, 'r')
        self.connection = mariadb.connect(
            user=user,
            password=pf.read()[:-1],
            host=host,
            port=3306,
            database=database,
        )
        pf.close()
        self.cursor = self.connection.cursor()
        logging.info(f'Connection with mariadb is established')

    def __del__(self):
        self.connection.close()
        logging.info(f'Connection with mariadb is closed')

    def populate_db(self, schema_file=os.path.join(DATA_PATH, 'schema.sql')):
        logging.info(f'Populating database')
        for line in open(schema_file, 'r'):
            self.cursor.execute(line)

    def insert_photo(self, user_id, emotion):
        logging.info(f'Inserting photo into DB user_id={user_id}')
        self.cursor.execute("INSERT INTO photos (user_id,emotion)" +
                            "VALUES (%s,%s)", (user_id, emotion))
        self.connection.commit()


if __name__ == '__main__':
    logging_format = '%(asctime)s %(levelname)s: %(message)s'
    logging_level = logging.INFO
    logging.basicConfig(level=logging_level, format=logging_format)

    logging.info('Creating DB manager')
    manager = DBManager()
    manager.populate_db()
    manager.insert_photo(0, 0)
    manager.insert_photo(1, 1)
    manager.insert_photo(2, 2)
