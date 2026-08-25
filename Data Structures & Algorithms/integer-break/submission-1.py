class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1]*(n+1)

        for i in range(1, n+1):
            for j in range(i):
                if (i-j) >= 1:
                    dp[i] = max(
                        dp[i], 
                        j * dp[i-j],
                        j * (i-j)
                    )

        return dp[n]