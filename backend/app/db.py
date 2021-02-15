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

        try:
                self.connection = mariadb.connect(
                    user=user,
                    password=pf.read()[:-1],
                    host=host,
                    port=3306,
                    database=database,
                )
                self.cursor = self.connection.cursor()
        except mariadb.Error as e:
            logging.error(f"Error connecting to MariaDB Platform: {e}")
        finally:
            logging.info(f'Connection with mariadb is established')

        pf.close()

    # def __del__(self):
    #     self.connection.close()
    #     logging.info(f'Connection with mariadb is closed')

    def populate_db(self, schema_file=os.path.join(DATA_PATH, 'schema.sql')):
        logging.info(f'Populating database')
        for line in open(schema_file, 'r'):
            self.cursor.execute(line)

    def insert_photo(self, user_id, emotion):
        if hasattr(self, 'cursor'):
            logging.info(f'Inserting photo into DB user_id={user_id}')
            try:
                self.cursor.execute("INSERT INTO photos (user_id,emotion)" +
                                    "VALUES (%s,%s)", (user_id, emotion))
            except mariadb.Error as e:
                logging.error(f"Error with mariadb: {e}")
            self.connection.commit()
        else:
            logging.error('Database is not connected')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s: %(message)s')
    logging.info('Creating DB manager')
    manager = DBManager()
    manager.populate_db()
