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

    def reverse(self):
        """把整条链表原地反转（不能新建链表）"""
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next  # 先保存下一个节点
            curr.next = prev  # 当前节点指向前面
            prev = curr  # prev往后挪
            curr = next_node  # curr往后挪
        self.head = prev  # 循环结束prev是新头节点

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.reverse()
ll.print_all()