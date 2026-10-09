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

# ═══ ① 按金额从大到小排序 ═══
cursor.execute("SELECT * FROM records ORDER BY amount DESC")
print("金额降序：", cursor.fetchall())

# ═══ ② 按金额从小到大排序 ═══
cursor.execute("SELECT * FROM records ORDER BY amount ASC")
print("金额升序：", cursor.fetchall())

# ═══ ③ 只取最贵的 2 笔 ═══
cursor.execute("SELECT * FROM records ORDER BY amount DESC LIMIT 2")
print("最贵的 2 笔：", cursor.fetchall())

conn.close()