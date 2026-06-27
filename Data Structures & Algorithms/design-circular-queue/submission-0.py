class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None] * k
        self.k = k
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull() and self.rear != self.k:
            self.arr[self.rear] = value
            self.rear += 1
            self.size += 1
            return True
        elif self.isFull():
            return False
        elif self.rear == self.k and not self.isFull():
            self.rear = 0
            self.arr[self.rear] = value
            self.rear += 1
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.front == (self.k-1):
                self.front = 0
                self.size -= 1
                return True
            else:
                self.front += 1
                self.size -= 1
                return True
        elif self.isEmpty():
            return False
            

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear - 1]

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