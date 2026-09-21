class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, v) -> int:
        while v != self.par[v]:
            self.par[v] = self.par[self.par[v]]
            v = self.par[v]

        return v

    def union(self, v1, v2) -> bool:
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        
        for i, e in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda e: e[2])

        mst_weight = 0
        uf = UnionFind(n)

        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w


        critical, pseudo = [], []

        for n1, n2, e_wei, i in edges:
            # without this edge
            uf = UnionFind(n)
            weight = 0
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w

            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue

            
            # force the edge
            uf = UnionFind(n)
            weight = e_wei
            uf.union(n1, n2)
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w

            if weight == mst_weight:
                pseudo.append(i)

        return [critical, pseudo]