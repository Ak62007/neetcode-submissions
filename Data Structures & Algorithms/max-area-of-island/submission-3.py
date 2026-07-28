class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        def bfs(i, j):
            nonlocal area
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))
            area += 1
            while q:
                row, col = q.pop()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)
                    if area > max_area:
                        max_area = area
                    area = 0

        return max_area