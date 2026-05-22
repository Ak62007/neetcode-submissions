class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maximum = 0

        while(i < j):
            if (min([heights[j], heights[i]]) * (j-i)) > maximum:
                print(j, i)
                maximum = min([heights[j], heights[i]]) * (j-i)
                print(maximum)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maximum