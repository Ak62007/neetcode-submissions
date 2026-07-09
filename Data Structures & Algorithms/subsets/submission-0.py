class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, ss):
            if i == len(nums):
                return res.append(ss)
            
            dfs(i + 1, ss + [nums[i]])
            dfs(i + 1, ss[:])
        
        dfs(0, [])

        return res
            