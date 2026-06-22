class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        for l in s:
            if not l == ']':
                ans.append(l)
            else:
                r_ch = ''
                while ans[-1] != '[':
                    r_ch = ans.pop() + r_ch
                ans.pop()
                times = ''
                while ans and (len(ans[-1]) == 1) and ord('0') <= ord(ans[-1]) <= ord('9'):
                    times = ans.pop() + times
                times = int(times)
                r_ch = times * r_ch
                ans.append(r_ch)
            
        return ''.join(ans)
                