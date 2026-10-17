class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        cache = {}
        def dfs(i, k):
            if i == len(nums):
                return 0

            if k == 1:
                return sum(nums[i:])
    
            if (i, k) in cache:
                return cache[(i, k)]

            min_max_sum, cur_sum  = float('inf'), 0
            for j in range(i, len(nums)-1):
                cur_sum += nums[j]
                if cur_sum > min_max_sum:
                    break
                min_max_sum = min(min_max_sum, max(cur_sum, dfs(j+1, k-1)))

            cache[(i, k)] = min_max_sum

            return cache[(i, k)]

        return dfs(0, k)