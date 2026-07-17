class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        units = set()
        def dfs(r, c):
            if (r <= -1 or c <= -1 or
                r >= ROWS or c >= COLS or 
                grid[r][c] == 0):
                return 1

            if (r, c) in units:
                return 0
            else:
                units.add((r, c))

            return dfs(r, c-1) + dfs(r, c+1) + dfs(r-1, c) + dfs(r+1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)