class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        indexes = set()
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = target - (nums[i] + nums[j])
                k = j + 1
                l = len(nums) - 1
                while(k < l):
                    if nums[k] + nums[l] == sum:
                        if (nums[i], nums[j], nums[k], nums[l]) in indexes:
                            pass
                        else:
                            indexes.add((nums[i], nums[j], nums[k], nums[l]))
                            ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                    elif nums[k] + nums[l] < sum:
                        k += 1
                    else:
                        l -= 1

        return ans