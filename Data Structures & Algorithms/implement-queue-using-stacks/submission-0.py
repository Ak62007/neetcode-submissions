class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.insert(0, x)

    def pop(self) -> int:
        if self.empty():
            return None
        else:
            return self.items.pop()

    def peek(self) -> int:
        if self.empty():
            return None
        else:
            return self.items[-1]


    def empty(self) -> bool:
        return True if len(self.items) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()