class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for var1, var2 in equations:
            adj[var1].append(var2)
            adj[var2].append(var1)

        divisions = {}

        for eq, div in zip(equations, values):
            divisions[(eq[0], eq[1])] = div
    
        def dfs(i, j, prev, ind):
            ans = -1
            for node in adj[i]:
                if node == prev:
                    continue
                elif node == j:
                    if (i, node) in divisions:
                        return ind * divisions[(i, node)]
                    elif (node, i) in divisions:
                        return ind * (1 / divisions[(node, i)])
                else:
                    if (i, node) in divisions:
                        ans = dfs(node, j, i, ind * divisions[(i, node)])
                        if ans != -1:
                            return ans
                    elif (node, i) in divisions:
                        ans = dfs(node, j, i, ind * (1 / divisions[(node, i)]))
                        if ans != -1:
                            return ans

            return ans

        ans = []

        for var1, var2 in queries:
            if var1 not in adj or var2 not in adj:
                ans.append(-1.0)
            elif var1 in adj and var2 in adj:
                if var1 == var2:
                    ans.append(1.0)
                else:
                    ans.append(dfs(var1, var2, '₹', 1))

            print(ans)

        
        return ans

        