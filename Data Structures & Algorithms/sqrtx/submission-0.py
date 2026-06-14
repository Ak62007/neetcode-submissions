class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        start = 0
        end = x//2
        mid = (start + end)//2

        while start <= end:
            if mid ** 2 < x:
                start = mid + 1
            elif mid ** 2 > x:
                end = mid - 1
            else:
                return mid

            mid = (start + end)//2

        return mid