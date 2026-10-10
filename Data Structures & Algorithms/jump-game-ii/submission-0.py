class Solution:
    def jump(self, nums: list[int]) -> int:
        target = len(nums) - 1
        no_of_jumps = 0
        while target != 0:
            temp = target
            cur = target
            for j in range(temp - 1, -1, -1):
                if target - j <= nums[j]:
                    cur = j

            no_of_jumps += 1
            target = cur

        return no_of_jumps
