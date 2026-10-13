# 1. 定义节点（一张纸条）
class Node:
    def __init__(self, value):
        self.value = value  # 纸条上写的内容（值）
        self.next = None  # 线索：下一个抽屉在哪（一开始没有，所以是 None）


# 2. 定义链表（寻宝游戏总控台）
class LinkedList:
    def __init__(self):
        self.head = None  # 游戏开始时，手里没有任何纸条（头节点为空）

    # 在末尾接一个新节点
    def append(self, value):
        new_node = Node(value)  # 造一张新纸条

        # 情况一：如果手里一张纸条都没有（空链表）
        if self.head is None:
            self.head = new_node  # 新纸条就是第一张（头节点）
            return  # 挂好了，直接结束，不用往下找了

        # 情况二：如果已经有纸条了，就从头开始顺着线索找
        current = self.head  # 拿住第一张纸条
        while current.next is not None:  # 只要当前纸条还有下一条线索
            current = current.next  # 顺着线索走到下一个抽屉
        # 循环结束，说明 current 已经是最后一张纸条了
        current.next = new_node  # 把新纸条挂上去

    # 从头到尾打印所有值
    def print_all(self):
        current = self.head  # 拿住第一张纸条
        while current is not None:  # 只要手里还有纸条
            print(current.value, end=" ")  # 打印纸条上的值，用空格隔开
            current = current.next  # 顺着线索走到下一个抽屉
        print()  # 全部打印完后，换行


# --- 测试代码 ---
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_all()  # 打印 1 2 3