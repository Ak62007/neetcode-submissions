class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1

        res = []
        perm = []

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for n in m:
                if m[n] > 0:
                    perm.append(n)
                    m[n] -= 1
                    backtrack()
                    m[n] += 1
                    perm.pop()

        backtrack()
        return res

            