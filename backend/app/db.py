import os
import sys
import logging
import mysql.connector as mariadb


try:
    PASSWORD = open('./mariadb-password.txt', 'r').read()[:-1]
except FileNotFoundError:
    logging.error(f'Password file not found. {SECRET_PATH}')
    sys.exit(1)

try:
    connection = mariadb.connect(
        user='root',
        password=PASSWORD,
        host='localhost',
        port=3306,
        database='ERProject'
    )
except mariadb.Error as e:
    logging.error(f'Can`t connect to mariadb {e}')
    sys.exit(1)

cursor = connection.cursor()

try:
    cursor.execute('SHOW TABLES')
except mariadb.Error as e:
    print(f'Error: {e}')

connection.close()
