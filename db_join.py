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

# ═══ ① 建分类表 ═══
cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        item VARCHAR(50) PRIMARY KEY,
        category VARCHAR(20)
    )
""")

cursor.execute("DELETE FROM categories")

cursor.executemany(
    "INSERT INTO categories (item, category) VALUES (%s, %s)",
    [
        ("吃饭", "餐饮"),
        ("奶茶", "餐饮"),
        ("打车", "交通"),
    ],
)

conn.commit()
print("分类表准备好了")

# ═══ ② 普通 JOIN ═══
print()
print("=== 普通 JOIN ===")

cursor.execute("""
    SELECT records.item, records.amount, categories.category
    FROM records
    JOIN categories ON records.item = categories.item
""")

for item, amount, category in cursor.fetchall():
    print(item, amount, category)

# ═══ ③ LEFT JOIN ═══
print()
print("=== LEFT JOIN ===")

cursor.execute("""
    SELECT records.item, records.amount, categories.category
    FROM records
    LEFT JOIN categories ON records.item = categories.item
""")

for item, amount, category in cursor.fetchall():
    print(item, amount, category)

conn.close()