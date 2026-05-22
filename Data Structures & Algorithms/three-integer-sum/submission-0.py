class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        indexes = set()
        for i in range(len(nums)):
            sum = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                if nums[j] + nums[k] == sum:
                    if (nums[i], nums[j], nums[k]) in indexes:
                        pass
                    else:
                        indexes.add((nums[i], nums[j], nums[k]))
                        ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif nums[j] + nums[k] < sum:
                    j += 1
                else:
                    k -= 1
        return ans