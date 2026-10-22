class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
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
    stack = Stack()

    matching_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'

    }
    for char in s:
        if char in "({[":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != matching_pairs[char]:
                return False
    return stack.is_empty()

if __name__ == "__main__":
    print(check("(a+b)"))
    print(check("((a+b)"))
    print(check("(a]"))
    print(check(""))