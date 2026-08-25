class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}
        def dfs(num):
            if num == 1:
                return 1

            if num in cache:
                return cache[num]

            max_prod = 1

            for i in range(1, num):
                if (num-i) >= 1:
                    max_prod = max(
                        max_prod, 
                        i * dfs(num-i),
                        i * (num-i)
                    )
            
            cache[num] = max_prod

            return max_prod

        return dfs(n)