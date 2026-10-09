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

# ═══ ① 先看清表里有什么 ═══
cursor.execute("SELECT id, item, amount FROM records")
print("表里所有记录：")
for row in cursor.fetchall():
    print("  ", row)

# ═══ ② 挑一个真实存在的 id ═══
target_id = 30          # ← 这个数字要按你上面的输出改

cursor.execute("SELECT id, item, amount FROM records WHERE id = %s", (target_id,))
print("改之前：", cursor.fetchone())

cursor.execute("UPDATE records SET amount = %s WHERE id = %s", (99, target_id))
conn.commit()

cursor.execute("SELECT id, item, amount FROM records WHERE id = %s", (target_id,))
print("改之后：", cursor.fetchone())

conn.close()