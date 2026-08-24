class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        total = 0
        for n in nums:
            total += n
            if total > ans:
                ans = total

            if total < 0:
                total = 0

        return ans