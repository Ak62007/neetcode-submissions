class Solution:
    def canJump(self, nums: list[int]) -> bool:
        cache = {}
        def dfs(src):
            if src == len(nums) - 1:
                return True
            if src in cache:
                return cache[src]

            for i in range(len(nums)-1, src, -1):
                step_size = i - src
                if step_size <= nums[src]:
                    if dfs(i):
                        cache[src] = True
                        return True

            cache[src] = False
            return cache[src]

        return dfs(0)