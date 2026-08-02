class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adjList = {i:[] for i in range(n)}
        for par, child in edges:
            adjList[par].append(child)
            adjList[child].append(par)

        cycle = set()

        def dfs(i, prev):
            if i in cycle:
                return False

            cycle.add(i)

            for node in adjList[i]:
                if node == prev:
                    continue
                else:
                    if not dfs(node, i): return False

            return True

        return dfs(0, -1) and (len(cycle) == n)
