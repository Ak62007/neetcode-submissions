class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))

            while q:
                row, col = q.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r ,c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == '1' and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
 
        ans = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in visited:
                    ans += 1
                    bfs(i, j)

        return ans