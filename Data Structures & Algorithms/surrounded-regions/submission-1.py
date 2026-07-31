class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(i, j):
            if (i not in range(ROWS) or
                j not in range(COLS) or
                (i, j) in visited or
                board[i][j] == 'X'):
                return

            if board[i][j] == 'O':
                visited.add((i, j))
                dfs(i, j-1)
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i-1, j)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited:
                    board[i][j] = 'X'