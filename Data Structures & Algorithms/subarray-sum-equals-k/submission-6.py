class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum = 0
        prefix_sum = {0 : 1}
        res = 0
        for num in nums: 
            cursum += num
            diff = cursum - k
            res += prefix_sum.get(diff, 0)
            prefix_sum[cursum] = 1 + prefix_sum.get(cursum, 0)

        return res