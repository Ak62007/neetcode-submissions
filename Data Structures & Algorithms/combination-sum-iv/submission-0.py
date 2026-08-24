class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(s):
            # if i >= len(nums):
            #     return 0

            if s in cache:
                return cache[s]

            total = 0
            for n in nums:
                if s + n < target:
                    cal = dfs(s + n)
                    cache[s + n] = cal
                    total += cal
                elif s + n == target:
                    total += 1
            
            return total

        return dfs(0)
