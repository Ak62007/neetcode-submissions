class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            num = nums[len(nums)-1]
            nums[1:len(nums)] = nums[0:(len(nums)-1)]
            nums[0] = num