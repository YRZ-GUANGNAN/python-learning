class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

q = Queue()
q.enqueue("小明")
q.enqueue("小红")
q.enqueue("小刚")

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())     