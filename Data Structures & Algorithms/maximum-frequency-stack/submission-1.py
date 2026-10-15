class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.max = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        val_cnt = self.cnt.get(val, 0) + 1
        self.cnt[val] = val_cnt
        if val_cnt > self.max:
            self.max = val_cnt
            self.stacks[val_cnt] = []
        
        self.stacks[val_cnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max].pop()
        self.cnt[res] -= 1

        if not self.stacks[self.max]:
            self.max -= 1

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()