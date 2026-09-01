class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        cache = {}

        def dfs(i, chance, m):
            if i >= len(piles):
                return 0

            if (i, chance, m) in cache:
                return cache[(i, chance, m)]

            count = 0
            if chance:
                s = 0
                total = 0

                for j in range(i, min(i+2*m, len(piles))):
                    count += 1
                    s += piles[j]
                    total = max(total, s + dfs(j+1, not chance, max(count, m)))

            else:
                total = float("inf")

                for j in range(i, min(i+2*m, len(piles))):
                    count += 1
                    total = min(total, dfs(j+1, not chance, max(count, m)))

            cache[(i, chance, m)] = total

            return cache[(i, chance, m)]

        return dfs(0, True, 1)

                    
