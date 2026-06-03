class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i, j = 0, k-1
        result = []
        while j < len(nums):
            result.append(max(nums[i:j+1]))
            i += 1
            j += 1

        return result