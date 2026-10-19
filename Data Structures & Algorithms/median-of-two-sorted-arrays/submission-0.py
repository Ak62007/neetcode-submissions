class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        nums1 += nums2
        print(nums1)
        nums1.sort()

        if len(nums1) % 2 == 0:
            idx = len(nums1) // 2
            return (nums1[idx-1] + nums1[idx]) / 2

        else:
            idx = len(nums1) // 2
            return nums1[idx]