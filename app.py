from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException, Header, Depends, Query
from pydantic import BaseModel
import pymysql
from config import db_password
import bcrypt
import jwt
import datetime
from contextlib import contextmanager

JWT_SECRET = "dev-secret-please-change-to-a-long-random-string-in-production"


class UserIn(BaseModel):
    username: str
    password: str


def current_user(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="未登录")
    token = authorization[7:]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="token 无效或已过期")
    return payload


app = FastAPI()


@app.get("/ui")
def ui():
    return FileResponse("index.html")


# ==================== 用 with 替代 try/finally ====================
@contextmanager
def db_conn():
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="learn",
        password=db_password,
        database="learn_db",
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        yield conn
    finally:
        conn.close()
# ================================================================


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
def list_records(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    user: dict = Depends(current_user),
):
    offset = (page - 1) * size

    with db_conn() as conn, conn.cursor() as cursor:
        cursor.execute(
            "SELECT id, item, amount, created_at FROM records "
            "WHERE user_id = %s ORDER BY id DESC LIMIT %s OFFSET %s",
            (user["user_id"], size, offset),
        )
        items = cursor.fetchall()

        cursor.execute(
            "SELECT COUNT(*) AS c FROM records WHERE user_id = %s",
            (user["user_id"],),
        )
        total = cursor.fetchone()["c"]

    return {
        "items": items,
        "total": total,
        "page": page,
        "size": size,
        "pages": (total + size - 1) // size,
    }


@app.post("/records")
def add_record(record: RecordIn, user: dict = Depends(current_user)):
    with db_conn() as conn, conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO records (item, amount, user_id) VALUES (%s, %s, %s)",
            (record.item, record.amount, user["user_id"]),
        )
        conn.commit()
        new_id = cursor.lastrowid

    return {"ok": True, "id": new_id}


@app.get("/summary")
def summary(user: dict = Depends(current_user)):
    with db_conn() as conn, conn.cursor() as cursor:
        cursor.execute(
            "SELECT COUNT(*) AS count, IFNULL(SUM(amount), 0) AS total "
            "FROM records WHERE user_id = %s",
            (user["user_id"],),
        )
        result = cursor.fetchone()

    return result


@app.delete("/records/{record_id}")
def delete_record(record_id: int, user: dict = Depends(current_user)):
    with db_conn() as conn, conn.cursor() as cursor:
        cursor.execute(
            "DELETE FROM records WHERE id = %s AND user_id = %s",
            (record_id, user["user_id"]),
        )
        conn.commit()
        deleted = cursor.rowcount

    if deleted == 0:
        raise HTTPException(status_code=404, detail="该记录不存在")

    return {"ok": True, "message": f"成功删除 id 为 {record_id} 的记录"}


@app.post("/register")
def register(user: UserIn):
    with db_conn() as conn, conn.cursor() as cursor:
        cursor.execute("SELECT id FROM users WHERE username = %s", (user.username,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="用户名已存在")

        password_hash = bcrypt.hashpw(
            user.password.encode(),
            bcrypt.gensalt(),
        ).decode()

        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (user.username, password_hash),
        )
        conn.commit()
        new_id = cursor.lastrowid

    return {"ok": True, "id": new_id}


@app.post("/login")
def login(user: UserIn):
    with db_conn() as conn, conn.cursor() as cursor:
        cursor.execute(
            "SELECT id, username, password_hash FROM users WHERE username = %s",
            (user.username,),
        )
        row = cursor.fetchone()

    if not row or not bcrypt.checkpw(user.password.encode(), row["password_hash"].encode()):
        raise HTTPException(status_code=401, detail="用户名或密码错误")

    payload = {
        "user_id": row["id"],
        "username": row["username"],
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=24),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")

    return {"token": token, "username": row["username"]}


@app.put("/records/{record_id}")
def update_record(record_id: int, record: RecordIn, user: dict = Depends(current_user)):
    with db_conn() as conn, conn.cursor() as cursor:
        cursor.execute(
            "UPDATE records SET item = %s, amount = %s WHERE id = %s AND user_id = %s",
            (record.item, record.amount, record_id, user["user_id"]),
        )
        conn.commit()
        updated = cursor.rowcount

    if updated == 0:
        raise HTTPException(status_code=404, detail="该记录不存在或不属于你")

    return {"ok": True, "id": record_id}