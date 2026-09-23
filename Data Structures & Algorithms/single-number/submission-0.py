class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = 0
        for num in nums:
            res ^= num

        return res 