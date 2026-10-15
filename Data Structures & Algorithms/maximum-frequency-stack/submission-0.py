class FreqStack:

    def __init__(self):
        self.heap_stack = []
        self.freq = {}
        self.idx = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        heapq.heappush(self.heap_stack, [-self.freq[val], -(self.idx), val])
        self.idx += 1
        

    def pop(self) -> int:
        val = heapq.heappop(self.heap_stack)[2]
        self.freq[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()