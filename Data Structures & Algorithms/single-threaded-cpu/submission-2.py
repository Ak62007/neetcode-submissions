class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_idx = []
        for i, task in enumerate(tasks):
            task_idx.append([task[0], task[1], i])

        task_idx.sort(key=lambda x: x[0])
        task_idx = deque(task_idx)

        batch = []
        order = []
        T = task_idx[0][0]
        while task_idx:
            while task_idx and task_idx[0][0] <= T:
                et, pt, i = task_idx.popleft()
                heapq.heappush(batch, [pt, i])

            if batch:
                pt, i = heapq.heappop(batch)
                order.append(i)
                T += pt
            else:
                T = task_idx[0][0]

        while batch:
            _, i = heapq.heappop(batch)
            order.append(i)

        return order