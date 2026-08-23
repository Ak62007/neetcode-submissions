class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minp, maxp = 1, 1

        for n in nums:
            if n == 0:
                minp, maxp = 1, 1
                continue
            else:
                tmp = n * maxp
                maxp = max(n * maxp, n * minp, n)
                minp = min(tmp, n * minp, n)

                res = max(res, maxp)

        return res