class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp_arr = [1]*n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp_arr[i] = max(dp_arr[j]+1, dp_arr[i])

        return max(dp_arr)