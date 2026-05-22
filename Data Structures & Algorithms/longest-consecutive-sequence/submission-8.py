class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        counts = []
        count = 0
        set_nums = set(nums)
        min_element = min(nums)
        while(i < (max(nums) - min(nums) + 1)):
            i += 1
            if min_element in set_nums:
                print(min_element)
                count+=1
                min_element += 1
            else:
                counts.append(count)
                count = 0
                min_element += 1
        counts.append(count)
        return max(counts)