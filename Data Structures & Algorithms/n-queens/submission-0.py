class Solution:
    def check(self, i, j):
        # same col
        for coor in self.queens_coor:
            r, c = coor
            # same col
            if c == j:
                return False
            # same dia
            if abs(r-i) == abs(c-j):
                return False

        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        # ROWS, COLS = n, n
        # self.board = [[False]*n for _ in range(n)]
        ans = []
        self.queens_coor = []

        def backtrack(q):
            if q == n:
                ans.append(self.queens_coor[:])
                # self.queens_coor = []
                return

            for c in range(n):
                if self.check(q, c):
                    self.queens_coor.append((q, c))
                    backtrack(q + 1)
                    self.queens_coor.pop()

        backtrack(0)

        final_ans = []
        for li in ans:
            li.sort(key=lambda x:x[0])
            ind_list = []       
            for coor in li:
                conf = ''
                qr, qc = coor
                for c in range(n):
                    if c == qc:
                        conf += "Q"
                    else:
                        conf += "."

                ind_list.append(conf)
            final_ans.append(ind_list)

        return final_ans
