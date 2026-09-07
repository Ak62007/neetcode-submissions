class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = {}

        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1

        task_heap = []
        for _, occ in task_map.items():
            task_heap.append(-occ)

        heapq.heapify(task_heap)
        
        T = 0
        task_q = deque()
        while task_heap or task_q:
            T += 1
            
            if task_heap:
                cur_task = 1 + heapq.heappop(task_heap)
                if cur_task:
                    task_q.append((cur_task, T + n))

            if task_q and task_q[0][1] == T:
                heapq.heappush(task_heap, task_q.popleft()[0])

        return T