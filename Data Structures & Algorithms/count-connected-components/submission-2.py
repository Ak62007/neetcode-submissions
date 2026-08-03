class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return

            visit.add(i)

            for node in adj[i]:
                if node == prev:
                    continue
                dfs(node, i)

        ans = 0
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                ans += 1
            if len(visit) == n:
                break
            
        return ans