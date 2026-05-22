class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        coordinates = [[[0,0], [2,2]], [[0,3], [2,5]], [[0,6], [2,8]], [[3,0], [5,2]], [[3,3], [5,5]], [[3,6], [5,8]], [[6,0], [8,2]], [[6,3], [8,5]], [[6,8], [8,8]]]
        n = len(board[0])

        def find_duplicates(r: list[str]) -> bool:
            extracted_str = "".join(r)
            extracted_str = extracted_str.split(".")
            extracted_str = "".join(extracted_str)
            
            return len(set(extracted_str)) != len(extracted_str)

        def check_columns() -> bool:
            columns = [board[i][j] for j in range(n) for i in range(n)]
            index = 0
            for i in range(9, 82, 9):
                if find_duplicates(columns[index:i]):
                    return True
                else:
                    index += 9 
                    continue
            return False

        def check_rows() -> bool:
            for i in range(n):
                if find_duplicates(board[i]):
                    return True
                else:
                    continue
            return False

        def check_mat(coordinates: list[list[list[int]]]) -> bool:
            for coordinate in coordinates:
                mat = []
                for r in range(coordinate[0][0], coordinate[1][0]+1):
                    for c in range(coordinate[0][1], coordinate[1][1]+1):
                        mat.append(board[r][c])
                if find_duplicates(mat):
                    return True
                else:
                    continue
            return False

        return not (check_rows() or check_columns() or check_mat(coordinates))
        
