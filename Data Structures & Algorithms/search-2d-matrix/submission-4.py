class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m*n - 1
        mid = (start + end)//2

        while start <= end:
            i = mid // n
            j = mid % n
        
            if matrix[i][j] < target:
                start = mid + 1
            elif matrix[i][j] > target:
                end = mid - 1
            else:
                return True

            mid = (start + end)//2

        return False