class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        arr = [i+1 for i in range(n)]
        print(arr)
        def dfs(i, cur):
            if len(cur) == k:
                res.append(cur[:])
                return
                
            if i >= n:
                return

            cur.append(arr[i])
            dfs(i+1, cur)

            cur.pop()
            dfs(i+1, cur)

        dfs(0, [])

        return res