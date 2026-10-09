

import pymysql
from config import db_password


conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="learn",
    password=db_password,
    database="learn_db",
)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT item, COUNT(*), SUM(amount)
    FROM records
    GROUP BY item
    ORDER BY SUM(amount) DESC
    """
)

for item, count, total in cursor.fetchall():
    print(f"{item}：{count} 笔， 共{total} 元")
conn.close()
