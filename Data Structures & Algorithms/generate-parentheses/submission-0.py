class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(used, cur):
            if used == n:
                res.append(cur)
                return

            for i in range(len(cur) + 1):
                cur_copy = cur
                cur = cur[:i] + "()" + cur[i:]
                used += 1
                dfs(used, cur)
                cur = cur_copy
                used -= 1

        dfs(0, "")

        return list(set(res))
            