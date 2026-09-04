class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}

        def dfs(choices):
            if len(choices) == 1:
                return choices[0]

            if choices in cache:
                return cache[choices]

            cp = list(choices)
            total = 0
            for i in range(len(choices)):
                cp.pop(i)
                if i-1 < 0:
                    total = max(total, 1 * choices[i] * choices[i+1] + dfs(tuple(cp)))
                elif i+1 == len(choices):
                    total = max(total, choices[i-1] * choices[i] * 1 + dfs(tuple(cp)))
                else:
                    total = max(total, choices[i-1] * choices[i] * choices[i+1] + dfs(tuple(cp)))

                cp = list(choices)

            cache[choices] = total

            return cache[choices]

        return dfs(tuple(nums))
