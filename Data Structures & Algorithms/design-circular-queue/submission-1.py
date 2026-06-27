class ListNode:
    def __init__(self, val = 0, nxt = None, prev = None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.right = ListNode()
        self.left = ListNode()
        self.left.nxt = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value, self.right, self.right.prev)
        self.right.prev.nxt = new_node
        self.right.prev = new_node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.nxt = self.left.nxt.nxt
        self.left.nxt.prev = self.left
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.nxt.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()