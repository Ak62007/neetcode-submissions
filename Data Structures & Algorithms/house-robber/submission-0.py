class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob = [0]*len(nums)
        rob[0] = nums[0]
        rob[1] = nums[1]

        for i in range(2, len(nums)):
            rob[i] = max(rob[:i-1]) + nums[i]

        return max(rob[-2], rob[-1])