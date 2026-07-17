class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        output = 0
        units = set()
        def dfs(r, c):
            nonlocal output
            if (r, c) in units:
                return 0
            else:
                units.add((r, c))
            if (r <= -1 or c <= -1 or
                r >= ROWS or c >= COLS or 
                grid[r][c] == 0):
                return 0

            if c-1 != -1:
                left = grid[r][c-1]
            else:
                left = 0
            if c+1 != COLS:
                right = grid[r][c+1]
            else:
                right = 0
            if r-1 != -1:
                up = grid[r-1][c]
            else:
                up = 0
            if r+1 != ROWS:
                down = grid[r+1][c]
            else:
                down = 0

            if left + right + up + down == 3:
                output += 1
            elif left + right + up + down == 2:
                output += 2
            elif left + right + up + down == 1:
                output += 3
            elif left + right + up + down == 0:
                output += 4

            dfs(r, c-1)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r+1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return output