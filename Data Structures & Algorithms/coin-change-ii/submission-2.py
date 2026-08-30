class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # tabulation

        if amount == 0:
            return 1

        COLS, ROWS = amount, 2

        dp = [[0]*(COLS+1) for _ in range(ROWS)]

        # base condition
        for r in range(ROWS):
            dp[r][-1] = 1

        # let's first calculate the last row
        for c in range(COLS-1, -1, -1):
            if c + coins[-1] < COLS+1:
                dp[ROWS-1][c] = dp[ROWS-1][c + coins[-1]]

        dp[0] = dp[1][:] 

        for r in range(len(coins)-2, -1, -1):
            for c in range(COLS-1, -1, -1):
                if c + coins[r] < COLS+1:
                    dp[0][c] = dp[0][c + coins[r]] + dp[1][c]
                else:
                    dp[0][c] = dp[1][c]

            dp[1] = dp[0][:]

        return dp[0][0]