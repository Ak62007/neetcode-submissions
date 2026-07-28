class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(i, j):
            if (i not in range(ROWS) or
                j not in range(COLS) or
                grid[i][j] == 0 or
                (i, j) in visited):
                return 0

            visited.add((i, j))
            return (1 + dfs(i+1, j) + 
                        dfs(i-1, j) + 
                        dfs(i, j+1) + 
                        dfs(i, j-1))


        for i in range(ROWS):
            for j in range(COLS):
                max_area = max(dfs(i, j), max_area)

        return max_area