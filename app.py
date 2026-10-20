from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pymysql
from config import db_password

app = FastAPI()



def get_conn():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="learn",
        password=db_password,
        database="learn_db",
        cursorclass=pymysql.cursors.DictCursor,
    )



class RecordIn(BaseModel):
    item: str
    amount: float




@app.get("/")
def root():
    return {"message": "你好，这是我的第一个 Web 服务"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"你好，{name}"}



@app.get("/records")
def list_records():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, item, amount, created_at FROM records ORDER BY id")
    rows = cursor.fetchall()
    conn.close()
    return rows



@app.post("/records")
def add_record(record: RecordIn):
    conn = get_conn()
    cursor = conn.cursor()

    sql = "INSERT INTO records (item, amount) VALUES (%s, %s)"
    cursor.execute(sql, (record.item, record.amount))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return {"ok": True, "id": new_id}



@app.get("/summary")
def summary():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS count, IFNULL(SUM(amount), 0) AS total FROM records")
    result = cursor.fetchone()
    conn.close()
    return result



@app.delete("/records/{record_id}")
def delete_record(record_id: int):
    conn = get_conn()
    cursor = conn.cursor()


    cursor.execute("DELETE FROM records WHERE id = %s", (record_id,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="该记录不存在")

    conn.close()
    return {"ok": True, "message": f"成功删除 id 为 {record_id} 的记录"}
