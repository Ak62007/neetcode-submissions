class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while(i < len(nums) and j < len(nums)):
            if nums[i] == nums[j]:
                nums.pop(i)
            else:   
                i += 1
                j += 1
        return len(nums)