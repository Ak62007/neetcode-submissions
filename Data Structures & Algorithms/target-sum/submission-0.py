class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, cur):
            if i == len(nums):
                if cur == target:
                    return 1
                else:
                    return 0

            # if cur > target:
            #     return 0
            
            if (i, cur) in cache:
                return cache[(i, cur)]

            pos, neg = 0, 0
            pos = dfs(i+1, cur + nums[i])
            neg = dfs(i+1, cur - nums[i])

            cache[(i, cur)] = pos + neg

            return cache[(i, cur)]

        return dfs(0, 0)