class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(i, j):
            if (i == ROWS-1) and (j == COLS-1):
                return grid[i][j]

            if (i, j) in dp:
                return dp[(i, j)]

            right, down = float('inf'), float('inf')
            if j+1 < COLS:
                right = dfs(i, j+1)
            if i+1 < ROWS:
                down = dfs(i+1, j)
            
            dp[(i, j)] = grid[i][j] + min(right, down)
            return dp[(i, j)]

        return dfs(0, 0)