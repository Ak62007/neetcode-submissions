class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        idx = [i for i in range(len(nums))]
        def backtrack(cur, idx):
            if not idx:
                if len(cur) == len(nums):
                    res.append(cur[:])
                return

            for i in idx[:]:
                cur.append(nums[i])
                idx.remove(i)
                backtrack(cur, idx)
                cur.pop()
                idx.append(i)

        backtrack([], idx)

        return res