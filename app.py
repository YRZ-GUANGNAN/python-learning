from fastapi import FastAPI, HTTPException # 引入了 HTTPException 用于报错
from pydantic import BaseModel
import json

FILE = "records.json"
app = FastAPI()


class RecordIn(BaseModel):
    item: str
    amount: float


def load_records():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_records(records):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


@app.get("/records")
def list_records():
    return load_records()


@app.get("/")
def root():
    return {"message": "你好，这是我的第一个 Web 服务"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"你好，{name}"}


@app.post("/records")
def add_record(record: RecordIn):
    records = load_records()
    records.append({"item": record.item, "amount": record.amount})
    save_records(records)
    return {"ok": True, "count": len(records)}



@app.get("/summary")
def summary():
    records = load_records()

    count = len(records)

    total = sum(r["amount"] for r in records)

    return {"count": count, "total": total}



@app.delete("/records/{index}")
def delete_record(index: int):
    records = load_records()


    if index < 0 or index >= len(records):

        raise HTTPException(status_code=404, detail="该记录不存在")


    deleted_record = records.pop(index)


    save_records(records)

    return {"ok": True, "deleted": deleted_record, "count": len(records)}
