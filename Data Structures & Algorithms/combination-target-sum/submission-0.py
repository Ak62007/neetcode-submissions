class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i, c_sum):
            if c_sum == target:
                res.append(subset[:])
                return
            
            if c_sum > target or i >= len(candidates):
                return
            subset.append(candidates[i])
            dfs(i, c_sum + candidates[i])
            # backtrack
            subset.pop()
            dfs(i + 1, c_sum)

        dfs(0, 0)
        return res
