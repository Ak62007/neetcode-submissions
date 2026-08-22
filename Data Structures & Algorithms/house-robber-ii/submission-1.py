class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 2:
            return max(nums)
        def house_robber(paisa: List[int]) -> int:
            n = len(paisa)
            dp = [0]*n

            dp[0] = paisa[0]

            for i in range(1, n):
                if i-2 < 0:
                    if paisa[i] > dp[i-1]:
                        dp[i] = paisa[i]
                    else:
                        dp[i] = dp[i-1]

                else:
                    dp[i] = max(dp[i-1], paisa[i] + dp[i-2])

            return dp[-1]


        return max(house_robber(nums[1:]), house_robber(nums[:n-1]))