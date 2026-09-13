class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # building the adj_list
        adj_list = defaultdict(list)

        for u, v, w in times:
            adj_list[u].append((w, v))

        min_heap = [[0, k]]
        heapq.heapify(min_heap)
        net_delays = {i+1:float("inf") for i in range(n)}
        net_delays[k] = 0
        visited = {i+1:False for i in range(n)}

        while min_heap:
            removed_delay, removed_ver = heapq.heappop(min_heap)
            visited[removed_ver] = True

            for p_dist, nei_vert in adj_list[removed_ver]:
                if visited[nei_vert]:
                    continue

                new_delay = removed_delay + p_dist

                if new_delay < net_delays[nei_vert]:
                    net_delays[nei_vert] = new_delay
                    heapq.heappush(min_heap, [new_delay, nei_vert])

        # print(net_delays)
        # print(visited)

        max_delay = max(net_delays.values())
        if max_delay != float("inf"):
            return max_delay
        return -1