import json

class todo:
    def __init__(self,title,done=False):
        self.title = title
        self.done = done
    def __str__(self):
        return f"[{'x' if self.done else ' '}] {self.title}"

FILE = "todo.json"
todos = []

try:
    with open(FILE,"r",encoding="utf-8") as f:
        data = json.load(f)
    for d in data:
        todos.append(todo(d["title"],d.get("done",False)))
except FileNotFoundError:
    pass

while True:
    print(" --- 当前待办 ---")
    for i in range(len(todos)):
        print(f"{i+1}.{todos[i]}")

    line = input("输入内容 输入q退出")
    if line.lower() == "q":
        break

    parts = line.split()

    if parts[0] == "done":
        idx = int(parts[1]) -1
        todos[idx].done = True
        print(f"已标记第{idx+1}项完成！")
    else:
        todos.append(todo(line))
        print("已添加！")

data = []
for t in todos:
    data.append({"title": t.title,"done":t.done})
with open(FILE,"w", encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)
print("已保存 再见")


