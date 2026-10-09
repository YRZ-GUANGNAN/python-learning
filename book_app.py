import pymysql
from config import db_password


def get_conn():
    """连接数据库。"""
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="learn",
        password=db_password,
        database="learn_db",
    )


def setup_table():
    """建表（已存在就跳过）。"""
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books ("
        "id INT AUTO_INCREMENT PRIMARY KEY, "
        "item VARCHAR(50), "
        "amount DECIMAL(10,2), "
        "created_at DATETIME DEFAULT CURRENT_TIMESTAMP"
        ")"
    )
    conn.commit()
    conn.close()


def add_record(item, amount):
    """记一笔。"""
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (item, amount) VALUES (%s, %s)",
        (item, amount),
    )
    conn.commit()
    conn.close()


def show_records():
    """查看所有记录。"""
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, item, amount, created_at FROM books ORDER BY id"
    )
    rows = cursor.fetchall()
    conn.close()

    if len(rows) == 0:
        print("还没有记录")
        return

    print()
    for rec_id, item, amount, created_at in rows:
        print(f"{rec_id}  {item}  {amount}  {created_at}")


def show_stats():
    """按项目统计。"""
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT item, COUNT(*), SUM(amount) "
        "FROM books "
        "GROUP BY item "
        "ORDER BY SUM(amount) DESC"
    )
    rows = cursor.fetchall()

    cursor.execute("SELECT SUM(amount) FROM books")
    total = cursor.fetchone()[0]

    conn.close()

    if len(rows) == 0:
        print("还没有记录")
        return

    print()
    for item, count, subtotal in rows:
        print(f"{item}：{count} 笔，共 {subtotal} 元")

    print()
    print(f"总计：{total} 元")


def delete_record():
    """删除一条记录。"""
    show_records()

    rec_id = input("\n要删除哪条？输入 id（直接回车取消）：")

    if rec_id == "":
        print("已取消")
        return

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (rec_id,))
    conn.commit()

    affected = cursor.rowcount
    conn.close()

    if affected == 0:
        print("没有找到这条记录")
    else:
        print("已删除")


def show_menu():
    print()
    print("=== 记账本 ===")
    print("1. 记一笔")
    print("2. 查看所有记录")
    print("3. 按项目统计")
    print("4. 删除记录")
    print("5. 退出")


# ══════════ 主程序 ══════════

setup_table()

while True:
    show_menu()
    choice = input("请选择：")

    if choice == "1":
        item = input("项目：")
        amount = float(input("金额："))
        add_record(item, amount)
        print("已记录")

    elif choice == "2":
        show_records()

    elif choice == "3":
        show_stats()

    elif choice == "4":
        delete_record()

    elif choice == "5":
        print("再见")
        break

    else:
        print("请输入 1-5 之间的数字")

    input("\n（按回车返回菜单）")
