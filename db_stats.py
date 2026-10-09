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

# ═══ ① 一共几笔 ═══
cursor.execute("SELECT COUNT(*) FROM records")
row = cursor.fetchone()
print("共", row[0], "笔")

# ═══ ② 总消费 ═══
cursor.execute("SELECT SUM(amount) FROM records")
row = cursor.fetchone()
print("总消费：", row[0])

# ═══ ③ 平均每笔 ═══
cursor.execute("SELECT AVG(amount) FROM records")
row = cursor.fetchone()
print("平均每笔：", row[0])

# ═══ ④ 最贵和最便宜 ═══
cursor.execute("SELECT MAX(amount), MIN(amount) FROM records")
row = cursor.fetchone()
print("最贵：", row[0], " 最便宜：", row[1])

conn.close() 