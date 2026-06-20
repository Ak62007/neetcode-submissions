class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        intme_stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while intme_stack and temp > intme_stack[-1][1]:
                fill_idx, stack_t = intme_stack.pop()
                ans[fill_idx] = i - fill_idx
            intme_stack.append((i, temp))
            
        return ans
