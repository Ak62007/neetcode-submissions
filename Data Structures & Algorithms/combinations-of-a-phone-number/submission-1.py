class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d_l = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        res = []
        cur = []

        def dfs(i):
            if len(cur) == len(digits):
                res.append("".join(cur[:]))
                return
            
            for l in d_l[digits[i]]:
                cur.append(l)
                dfs(i + 1)
                cur.pop()

        dfs(0)

        return res