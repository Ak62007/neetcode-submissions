class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # tabulation

        if amount == 0:
            return 1

        ROWS, COLS = len(coins), amount

        dp = [[0]*(COLS+1) for _ in range(ROWS)]

        # base condition
        for r in range(ROWS):
            dp[r][-1] = 1

        for c in range(COLS-1, -1, -1):
            for r in range(ROWS-1, -1, -1):
                if r+1 < ROWS:
                    prev_comb = dp[r+1][c]
                else:
                    prev_comb = 0

                if (c + coins[r]) < COLS+1:
                    dp_prev = dp[r][c + coins[r]]
                else:
                    dp_prev = 0

                dp[r][c] = prev_comb + dp_prev

        # print(dp)

        return dp[0][0]