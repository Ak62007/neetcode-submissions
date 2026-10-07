class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        global_max = float('-inf')
        global_min = float('inf')

        cur_max = 0
        cur_min = 0

        total = 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)

            global_max = max(global_max, cur_max)
            global_min = min(global_min, cur_min)

            total += num

        return max(global_max, total - global_min) if global_max > 0 else global_max