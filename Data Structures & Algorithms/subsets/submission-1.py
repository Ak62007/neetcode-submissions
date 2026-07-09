class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i == len(nums):
                return res.append(subset[:])
            
            subset.append(nums[i])
            dfs(i+1)
            # backtrack
            subset.pop()
            dfs(i+1)
        
        dfs(0)

        return res
            