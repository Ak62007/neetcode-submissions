class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        grid = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            grid[i][0] = i

        for i in range(n+1):
            grid[0][i] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    grid[i][j] = grid[i-1][j-1]
                else:
                    grid[i][j] = 1 + min(grid[i-1][j], grid[i][j-1], grid[i-1][j-1])

        return grid[m][n]