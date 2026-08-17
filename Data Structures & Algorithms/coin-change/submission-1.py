class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # min_no = float('inf')
        cache = {}
        def dfs(amt):
            if amt in cache:
                return cache[amt]

            if amt == 0:
                return 0

            min_no = float('inf')
            for coin in coins:
                if amt >= coin:
                    result = dfs(amt-coin)

                    if result != float('inf'):
                        min_no = min(min_no, 1 + result)

            cache[amt] = min_no
            return min_no

        ans = dfs(amount)

        return ans if ans != float('inf') else -1
