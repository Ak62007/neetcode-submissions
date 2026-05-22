from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not (len(nums) > len(set(nums))):
            return False
        mapping  = defaultdict(list)
        for i in range(len(nums)):
            if len(mapping[nums[i]]) == 0:
                mapping[nums[i]].append(i)
            else:
                if abs(mapping[nums[i]][0] - i) <= k:
                    return True
                else:
                    mapping[nums[i]] = [i]

        return False

        # # print(mapping)
        # for key in mapping.keys():
        #     if len(mapping[key]) > 1:
        #         if (max(mapping[key]) - min(mapping[key])) <= k:
        #             return True
        #     else:
        #         continue
        
        # return False
