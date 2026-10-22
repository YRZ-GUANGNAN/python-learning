from contextlib import contextmanager

import pymysql

from config import db_password


def get_conn():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="learn",
        password=db_password,
        database="learn_db",
        cursorclass=pymysql.cursors.DictCursor,
    )


@contextmanager
def db_conn():
    conn = get_conn()
    try:
        yield conn
    finally:
        conn.close()