class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()


    def delete(self, value):
        """删掉第一个值等于 value 的节点。没找到就什么都不做。"""

        if self.head is None:
            return


        if self.head.value == value:
            self.head = self.head.next
            return


        prev = None
        curr = self.head

        while curr is not None:
            if curr.value == value:

                prev.next = curr.next
                return
            else:

                prev = curr
                curr = curr.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.delete(2)
ll.print_all()