class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        edge_cnt = {}
        leaves = deque()
        for node, nei in adj.items():
            if len(nei) == 1:
                leaves.append(node)
            edge_cnt[node] = len(nei)

        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)