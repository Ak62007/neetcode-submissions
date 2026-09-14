class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = {i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append((cost, j))
                adj[j].append((cost, i))


        # pirm's algo
        tc = 0
        min_heap = [[0, 0]]
        visited = set()

        while len(visited) < N:
            cost, cur = heapq.heappop(min_heap)
            if cur in visited:
                continue
            tc += cost
            visited.add(cur)

            for neiCost, nei in adj[cur]:
                if nei not in visited:
                    heapq.heappush(min_heap, [neiCost, nei])

        return tc
