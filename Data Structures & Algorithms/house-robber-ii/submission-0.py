class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        dp1 = [0]*n
        dp2 = [0]*n

        dp1[0] = nums[0]
        dp2[1] = nums[1]

        for i in range(1, n):
            if i-2 < 0:
                if nums[i] < dp1[i-1]:
                    dp1[i] = dp1[i-1]
                else:
                    dp1[i] = nums[i]
            else:
                dp1[i] = max(dp1[i-1], nums[i] + dp1[i-2])
                dp2[i] = max(dp2[i-1], nums[i] + dp2[i-2])

        # print(dp1)
        # print(dp2)

        return max(dp1[-2], dp2[-1])
