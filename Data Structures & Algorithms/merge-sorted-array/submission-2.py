class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while(i < (m+n)):
            if j < n:
                if nums1[i] < nums2[j]:
                    i += 1
                    print(nums1)
                else:
                    nums1[i+1:m+j+1] = nums1[i:m+j]
                    print(nums1)
                    nums1[i] = nums2[j]
                    i+=1
                    j+=1
            else:
                break

        if j <= (n-1):
            nums1[m+j: m+n] = nums2[j:n]
            print("hii")
        # nums1[m:m+n+1] = nums2