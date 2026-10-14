class Solution:
    def checkValidString(self, s: str) -> bool: 

        stack = []
        as_cnt = []

        for i, l in enumerate(s):
            if stack:
                if l == '(':
                    if stack[-1][0] == ')':
                        stack.pop()
                    elif stack[-1][0] == '(':
                        stack.append(('(', i))
                elif l == ')':
                    if stack[-1][0] == '(':
                        stack.pop()
                    elif stack[-1][0] == ')':
                        stack.append((')', i))
                else:
                    as_cnt.append(i)
            else:
                if l == '*':
                    as_cnt.append(i)
                elif l == ')':
                    if as_cnt:
                        as_cnt.pop()
                    else:
                        return False
                else:
                    stack.append(('(', i))

        while stack:
            if as_cnt:
                if stack[-1][1] < as_cnt[-1]:
                    stack.pop()
                    as_cnt.pop()
                else:
                    return False
            else:
                return False

        return True