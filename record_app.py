import json

class Record:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    def __str__(self):
        return f"{self.item} {self.amount:.0f} 元"

FILE = "records.json"

records = []
try:
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    for d in data:
        records.append(Record(d["item"], d["amount"]))
except FileNotFoundError:
    pass

while True:
    line = input("记账（项目 金额），输入 q 退出：")
    if line.lower() == 'q':
        break

    parts = line.split()
    # 这个是把字符串切开的
    item = parts[0]
    amount = float(parts[1])
    records.append(Record(item, amount))
    # 将用户的输入转成项目和金额

data = []
for r in records:
    data.append({"item": r.item, "amount": r.amount})

with open(FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total = 0
for r in records:
    print(r)
    total += r.amount
print(f"总计 {total:.0f} 元")

# 吃饭吃饭吃饭吃饭
# 优化版本
import json

class Record:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    def __str__(self):
        return f"{self.item} {self.amount:.0f} 元"

FILE = "records.json"


records = []
try:
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    records = [Record(d["item"], d["amount"]) for d in data]
except FileNotFoundError:
    pass

while True:
    line = input("记账（项目 金额），输入 q 退出：")
    if line.lower() == 'q':
        break

    parts = line.split()
    if len(parts) == 2:
        item = parts[0]
        amount = float(parts[1])
        records.append(Record(item, amount))
    else:
        print("输入格式不对，请用空格隔开（例如：吃饭 20）")


data = [{"item": r.item, "amount": r.amount} for r in records]

with open(FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


for r in records:
    print(r)


total = sum(r.amount for r in records)
print(f"总计 {total:.0f} 元")