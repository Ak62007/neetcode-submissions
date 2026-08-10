class Solution:
    def __init__(self):
        self.map = {}
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        elif n in self.map:
            return self.map[n]

        answer = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.map[n] = answer
        return answer