class Record:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    def __str__(self):
        return f"{self.item} {self.amount} 元"


records = [
    Record("吃饭", 25),
    Record("打车", 13),
    Record("奶茶", 18),
    Record("买书", 45),
]


sorted_by_amount = sorted(records, key=lambda r: r.amount)

print("--- 按金额升序 ---")
for r in sorted_by_amount:
    print(r)


sorted_by_amount_desc = sorted(records, key=lambda r: r.amount, reverse=True)

print("\n--- 按金额降序 ---")
for r in sorted_by_amount_desc:
    print(r)



sorted_by_name_len = sorted(records, key=lambda r: len(r.item))

print("\n--- 按项目名称长度排序 ---")
for r in sorted_by_name_len:
    print(r)