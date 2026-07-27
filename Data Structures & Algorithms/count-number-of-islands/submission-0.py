class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(i, j):
            if (i < 0 or i >= ROWS or
                j < 0 or j >= COLS):
                return

            if (i, j) in visited or grid[i][j] == '0':
                return

            if grid[i][j] == '1' and (i, j) not in visited:
                visited.add((i, j))

            dfs(i, j + 1)
            dfs(i, j-1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        ans = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in visited:
                    ans += 1
                    dfs(i, j)

        return ans