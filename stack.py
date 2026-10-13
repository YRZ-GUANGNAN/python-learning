# brackets.py

class Stack:
    """自己实现的栈类"""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def check(s: str) -> bool:
    """检查字符串中的括号是否匹配"""
    # 创建一个栈实例
    stack = Stack()

    # 定义匹配规则
    matching_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        # 如果是左括号，入栈
        if char in "([{":
            stack.push(char)
        # 如果是右括号
        elif char in ")]}":
            # 如果栈为空，说明没有对应的左括号
            if stack.is_empty():
                return False
            # 弹出栈顶元素
            top = stack.pop()
            # 检查是否与当前右括号匹配
            if top != matching_pairs[char]:
                return False

    # 遍历结束后，如果栈为空，说明所有括号都匹配成功
    return stack.is_empty()



if __name__ == "__main__":
    print(check("(a+b)"))  # True
    print(check("((a+b)"))  # False
    print(check("(a]"))  # False
    print(check(""))  # True