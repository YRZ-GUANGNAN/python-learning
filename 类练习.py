class Record:
    def __init__(self,item,amount):
        self.item = item
        self.amount = amount

    def show(self):
        print(f"{self.item} {self.amount} 元")

    def add(self, x):
        self.amount += x
         # 期望打印：吃饭 30 元
    def __str__(self):
        return f"{self.item} {self.amount} 元"
r = Record("吃饭", 25)
print(r)              # 走 __str__ → 吃饭 25 元
print(r.show())       # 走 show，但会多打一行
r1 = Record("吃饭", 25)
r2 = Record("打车", 13)
r1.add(5)
r1.show()        # 直接改 r1 的 amount

print(r1.amount)      # 这两行分别打印什么？
print(r2.amount)

total = 0
records = []

records.append(Record("吃饭",25))
records.append(Record("打车",13))
records.append(Record("奶茶",18))
for r in records:
    r.show()
    total += r.amount
print(f"总计 {total} 元")
