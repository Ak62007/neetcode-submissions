class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        q = collections.deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        def addRoom(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] == -1 or
                (r, c) in visited):
                return

            q.append((r, c))
            visited.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addRoom(r-1, c)
                addRoom(r+1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)

            dist += 1

