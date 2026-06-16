class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_v = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                min_v = min(min_v, nums[l])
                break

            m = (l + r)//2
            min_v = min(min_v, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return min_v

            

            
