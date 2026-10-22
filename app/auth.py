import jwt
from fastapi import Header, HTTPException

JWT_SECRET = "dev-secret-please-change-to-a-long-random-string-in-production"


def current_user(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="未登录")

    token = authorization[7:]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="token 无效或已过期")

    return payload