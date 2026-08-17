class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)

        if nums_sum % 2 != 0:
            return False

        target = nums_sum // 2
        dp = [False]*(target+1)
        dp[0] = True

        for num in nums:
            for i in range(target-num, -1, -1):
                if dp[i]:
                    dp[i + num] = True

        return dp[-1]