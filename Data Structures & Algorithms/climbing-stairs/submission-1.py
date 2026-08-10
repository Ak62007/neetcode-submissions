class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        table = [0]*(n+1)
        # knows
        table[1] = 1
        table[2] = 2

        for i in range(3, len(table)):
            table[i] = table[i-1] + table[i-2]

        return table[-1]