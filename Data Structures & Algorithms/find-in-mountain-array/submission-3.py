# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        s, e = 0, n-1
        while s < e:
            mid = s + (e - s) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                s = mid + 1
            else:
                e = mid
        
        print(mid)
        peak = mid
        # binary search in the first part
        s, e = 0, peak
        while s <= e:
            mid = s + ((e - s) // 2)
            if mountainArr.get(mid) == target:
                break
            elif mountainArr.get(mid) < target:
                s = mid + 1
            else:
                e = mid - 1

        if mountainArr.get(mid) != target:
            # binary search on the second half
            s, e = peak+1, n-1
            while s <= e:
                mid = s + ((e - s) // 2)
                if mountainArr.get(mid) == target:
                    break
                elif mountainArr.get(mid) < target:
                    e = mid - 1
                else:
                    s = mid + 1

            if mountainArr.get(mid) != target:
                return -1
            else:
                return mid
        else:
            return mid
        # return 0