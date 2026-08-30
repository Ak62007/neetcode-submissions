class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        if amount == 0:
            return 1

        cache = {}
        def dfs(i, amt):
            if amt == amount:
                return 1
            if amt > amount or i == len(coins):
                return 0 

            if (i, amt) in cache:
                return cache[(i, amt)]

            take = dfs(i, amt + coins[i])
            skip = dfs(i+1, amt)

            cache[(i, amt)] = take + skip

            return cache[(i, amt)]

        # total = 0
        # for i in range(len(coins)):
        #     total += dfs(i, coins[i])

        return dfs(0, 0)
            