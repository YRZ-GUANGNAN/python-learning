from fastapi.responses import FileResponse
from fastapi import FastAPI

from app.routers import records, users

app = FastAPI()

app.include_router(users.router)
app.include_router(records.router)


@app.get("/ui")
def ui():
    return FileResponse("index.html")


@app.get("/")
def root():
    return {"message": "你好，这是我的第一个 Web 服务"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"你好，{name}"}