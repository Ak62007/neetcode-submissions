class Solution:
    def __init__(self):
        self.map = {}
    def climbStairs(self, n: int) -> int:
        # using memoization
        if n in self.map:
            return self.map[n]
        # base cases
        if n == 1:
            return 1

        if n == 2:
            return 2

        answer = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.map[n] = answer

        return answer