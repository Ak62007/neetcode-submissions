check = lambda x, y: True if f"{x}{y}" in ["()", "{}", "[]"] else False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            else:
                if check(stack[-1], ch):
                    stack.pop()
                else:
                    stack.append(ch)
        
        if len(stack) == 0:
            return True
        else:
            return False