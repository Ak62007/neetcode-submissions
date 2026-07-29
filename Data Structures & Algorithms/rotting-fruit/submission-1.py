class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def addCell(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] == 0 or
                (r, c) in visited):
                return

            q.append((r, c))
            visited.add((r, c))


        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        fresh = False
        q = collections.deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                elif not fresh:
                    if grid[i][j] == 1:
                        fresh = True

        if not q and fresh:
            return -1
        elif (q and not fresh) or (not q and not fresh):
            return 0
        
        minutes = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            minutes += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return minutes
