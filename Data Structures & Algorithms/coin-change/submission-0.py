class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0]*(amount+1)
        for i in range(1, len(dp)):
            to_use = []
            for coin in coins:
                if coin <= i:
                    if i-coin != 0 and dp[i-coin] == 0:
                        continue
                    to_use.append(dp[i-coin])
            if to_use:
                dp[i] = 1 + min(to_use)
            else:
                dp[i] = 0
        return dp[-1] if dp[-1] != 0 else -1