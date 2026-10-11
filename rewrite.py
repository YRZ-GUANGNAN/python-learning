import json
from datetime import datetime
class Record:
    def __init__(self,item,amount,time=None):
            self.item = item
            self.amount = amount

            if time is None:
                self.time = datetime.now().strftime("%Y-%m-%d %H:%M")
            else:
                self.time = time

    def __str__(self):
        return f"{self.item} {self.amount:.0f}元 {self.time}"

FILE = "records.json"

records = []
try:
    with open(FILE, "r", encoding="UTF-8") as f:
        data = json.load(f)
    for d in data:
        records.append(Record(d["item"], d["amount"],d["time"]))
except FileNotFoundError:
    pass

while True:
    line = input("请输入项目 金额  输入q退出")
    if line.lower() == "q":
        break

    parts =line.split()
    item = parts[0]
    amount = float(parts[1])
    records.append(Record(item, amount,))

data = []
for r in records:
    data.append({"item":r.item,"amount":r.amount,"time":r.time})

with open(FILE,"w",encoding="UTF-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2 )
total = 0
for r in records:
    print(r)
    total += r.amount
print(f"{total:.0f}元")













