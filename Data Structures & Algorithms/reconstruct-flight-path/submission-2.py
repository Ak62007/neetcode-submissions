class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj_list = defaultdict(list)

        # Reverse sorting
        tickets.sort(reverse=True)

        for src, dest in tickets:
            adj_list[src].append(dest)

        res = []

        def dfs(src):
            while adj_list[src]:
                nei = adj_list[src].pop()
                dfs(nei)

            res.append(src)

        dfs("JFK")

        return res[::-1]