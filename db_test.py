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

# ═══ ① 清空表（避免数据重复累积）═══
cursor.execute("DELETE FROM records")
conn.commit()

# ═══ ② 插入 4 条 ═══
cursor.executemany(
    "INSERT INTO records (item, amount) VALUES (%s, %s)",
    [
        ("打车", 18),
        ("奶茶", 12),
        ("吃饭", 30),
        ("打车", 22),
    ],
)

conn.commit()
print("插入完成")

# ═══ ③ 三种查询 ═══
cursor.execute("SELECT * FROM records")
print("全部：", cursor.fetchall())

cursor.execute("SELECT * FROM records WHERE item = %s", ("吃饭",))
print("吃饭：", cursor.fetchall())

cursor.execute("SELECT * FROM records WHERE amount > %s", (20,))
print(">20：", cursor.fetchall())

conn.close()