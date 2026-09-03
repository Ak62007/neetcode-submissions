class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i, cur):
            if i == len(s):
                if len(cur) == len(t) and cur == t:
                    return 1
                else:
                    return 0

            if cur == t:
                return 1

            if (len(cur) < len(t) and cur != t[:len(cur)]) or (len(cur) > len(t)):
                return 0

            if (i, cur) in cache:
                return cache[(i, cur)]

            total = 0

            # include
            total += dfs(i+1, cur + s[i])

            # skip
            total += dfs(i+1, cur)

            cache[(i, cur)] = total

            return cache[(i, cur)]

        return dfs(0, '')