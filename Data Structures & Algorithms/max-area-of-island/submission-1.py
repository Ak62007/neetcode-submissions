class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        def dfs(i, j):
            nonlocal area
            if (i not in range(ROWS) or 
                j not in range(COLS) or
                grid[i][j] == 0 or
                (i, j) in visited):
                return

            area += 1

            visited.add((i, j))

            dfs(i , j + 1)
            dfs(i , j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j)
                    if area > max_area:
                        max_area = area
                    area = 0

        return max_area