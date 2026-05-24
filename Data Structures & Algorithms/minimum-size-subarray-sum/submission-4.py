class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        min_len = []
        ssa = nums[0]
        switch = True
        flag = True
        while flag:
            if (i == len(nums)-1) and (j == len(nums)-1):
                if len(nums) == 1:
                    if ssa >= target:
                        return 1

            if switch == True:
                
                while ssa < target:
                    if j < len(nums)-1:
                        j += 1
                        ssa += nums[j]
                    else:
                        break

                if ssa >= target:
                    switch = False
                else:
                    flag = False                    
                
            else:
                 
                while ssa >= target:
                    if i < j:
                        ssa -= nums[i]
                        i += 1
                    else:
                        break
                
                if ssa < target:
                    switch = True
                    min_len.append(j - i + 2)
                else:
                    return 1

        if len(min_len) == 0:
            return 0
        else:
            return min(min_len)
                

