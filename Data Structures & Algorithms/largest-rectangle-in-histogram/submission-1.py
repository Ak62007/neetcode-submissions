class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_cum = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, hei = stack.pop()
                max_cum = max(max_cum, hei * (i - idx))
                start = idx 

            stack.append((start, h))

        for i, h in stack:
            max_cum = max(max_cum, h * (len(heights) - i))

        return max_cum
                