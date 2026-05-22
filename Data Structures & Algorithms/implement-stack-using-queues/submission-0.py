class MyStack:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        else:
            return self.items.pop()

    def top(self) -> int:
        if self.empty():
            return None
        else:
            return self.items[-1]

    def empty(self) -> bool:
        return True if len(self.items) == 0  else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()