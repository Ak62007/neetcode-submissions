class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        # m = {i:chr(64+i) for i in range(1, 27)}
        # no_of_ways = 0
        cache = {}

        def recur(i):
            if i in cache:
                return cache[i]

            if i >= len(s):
                return 1

            flag1, flag2 = 0, 0

            if s[i] != '0' and (ord('1') <= ord(s[i]) <= ord('9')):
                flag1 = recur(i + 1)

            if i+2 <= len(s):
                if s[i] != '0' and (10 <= int(s[i:i+2]) <= 26):
                    flag2 = recur(i + 2)

            cache[i] = flag1 + flag2
            
            return flag1 + flag2

        return recur(0)