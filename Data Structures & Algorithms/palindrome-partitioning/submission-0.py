class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part[:])

            for j in range(i, len(s)):
                ss = s[i:j + 1]
                if ss == ss[::-1]:
                    part.append(ss)
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res