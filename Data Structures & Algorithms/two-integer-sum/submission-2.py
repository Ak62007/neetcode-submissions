class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            if (target-nums[i]) in mapping.keys():
                return [mapping[target-nums[i]], i]
            else:
                mapping[nums[i]] = i

