class UnionFind:
    def __init__(self, n:int):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n1: int):
        res = n1
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]

        return res

    def union(self, n1: int, n2: int):
        p1, p2 = self.find(n1), self.find(n2)

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))

        mailToIdx = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in mailToIdx:
                    uf.union(i, mailToIdx[e])
                else:
                    mailToIdx[e] = i

        emailGroups = defaultdict(list)

        for e, i in mailToIdx.items():
            leader = uf.find(i)
            emailGroups[leader].append(e)

        ans = []
        for i, eg in emailGroups.items():
            name = accounts[i][0]
            ans.append([name] + sorted(eg))

        return ans