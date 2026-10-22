import bcrypt
import datetime

import jwt
from fastapi import APIRouter, HTTPException

from app.auth import JWT_SECRET
from app.db import db_conn
from app.schemas import UserIn

router = APIRouter()


@router.post("/register")
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


@router.post("/login")
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