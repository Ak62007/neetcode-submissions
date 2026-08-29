class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        cache = {}
        def dfs(i, buy, sell):
            if i == len(prices):
                return 0

            if (i, buy, sell) in cache:
                return cache[(i, buy, sell)]

            if sell:
                # cooldown
                total = dfs(i+1, False, False)

            elif buy:
                # sell or not sell
                total =  max(prices[i] + dfs(i+1, False, True),
                            dfs(i+1, True, False))
            else:
                # buy or not buy
                total = max(-prices[i] + dfs(i+1, True, False), 
                            dfs(i+1, False, False))
            
            cache[(i, buy, sell)] = total
            return cache[(i, buy, sell)]

        return dfs(0, False, False)
                