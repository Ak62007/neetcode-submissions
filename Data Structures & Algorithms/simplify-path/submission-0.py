from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        s_stack = []
        for l in path:
            if s_stack:
                if (s_stack[-1] == '/') and (l == '/'):
                    s_stack.pop()
                    s_stack.append(l)
                else:
                    s_stack.append(l)
            else:
                s_stack.append(l)

        cleaned_path = "".join(s_stack)
        # print(cleaned_path)

        cleaned_path = cleaned_path.split('/')
        print(cleaned_path)

        for l in cleaned_path:
            if l == '':
                continue
            elif l == '.':
                continue
            elif l == '..':
                if len(ans) < 2:
                    ans = []
                else:
                    ans.pop()
                    ans.pop()
            else:
                ans.append('/')
                ans.append(l)

        if ans:
            return "".join(ans)
        else:
            return '/'