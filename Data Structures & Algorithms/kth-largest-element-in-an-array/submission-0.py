class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        ans = 0
        for _ in range(len(nums) - k + 1):
            ans = heapq.heappop(nums)

        return ans