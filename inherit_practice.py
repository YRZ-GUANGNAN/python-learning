
class Record:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    def describe(self):
        return f"{self.item} {self.amount} 元"



class Expense(Record):
    def describe(self):
        return f"支出：{self.item} -{self.amount} 元"



class Income(Record):
    def describe(self):
        return f"收入：{self.item} +{self.amount} 元"



if __name__ == "__main__":

    records = [
        Expense("吃饭", 25),
        Income("奖学金", 5000),
        Expense("打车", 13),
    ]


    for r in records:
        print(r.describe())