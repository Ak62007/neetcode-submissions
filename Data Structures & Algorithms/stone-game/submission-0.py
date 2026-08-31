class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        def dfs(i, j, chance, a, b):
            if len(piles[i:j+1]) == 0:
                return a > b

            if (i, j) in cache:
                return cache[(i, j)]

            res = False
            
            if len(piles[i:j+1]) == 1:
                if chance:
                    res = dfs(i+1, j, not chance, a + piles[i], b)
                else:
                    res = dfs(i+1, j, not chance, a, b + piles[i])

            elif len(piles[i:j+1]) > 1:
                c1 = piles[i]
                c2 = piles[j]

                if chance:
                    res = (dfs(i+1, j, not chance, a + c1, b) or 
                    dfs(i, j-1, not chance, a + c2, b))

                else:
                    res = (dfs(i+1, j, not chance, a, b + c1) or 
                    dfs(i, j-1, not chance, a, b + c2))

            cache[(i, j)] = res
            return cache[(i, j)]

        return dfs(0, len(piles)-1, True, 0, 0)
            