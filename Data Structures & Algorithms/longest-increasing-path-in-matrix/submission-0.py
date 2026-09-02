class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        cache = {}

        def dfs(i, j):
            if i < 0 or i == ROWS or j < 0 or j == COLS:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            total = 1

            # left
            if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                total = max(total, 1 + dfs(i, j-1))

            # right
            if j+1 < COLS and matrix[i][j+1] > matrix[i][j]:
                total = max(total, 1 + dfs(i, j+1))

            # up
            if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                total = max(total, 1 + dfs(i-1, j))

            # down
            if i+1 < ROWS and matrix[i+1][j] > matrix[i][j]:
                total = max(total, 1 + dfs(i+1, j))

            cache[(i, j)] = total
            return cache[(i, j)]

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i, j))
                # print(f"For ({i}, {j}): current res: {res}")
                # print(f"cache state: {cache}")

        return res