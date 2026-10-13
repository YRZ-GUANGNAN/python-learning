# 栈类定义
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0



def check(s):
    stack = Stack()
    matching_pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != matching_pairs[ch]:
                return False

    return stack.is_empty()


print(check("(a+b)"))
print(check("((a+b)"))
print(check("(a]"))
print(check(""))

