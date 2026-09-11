class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        for profit, capital in zip(profits, capital):
            heap.append([-profit, capital])

        heapq.heapify(heap)

        # output = 0

        while True:
            storage = []
            if k > 0:
                while heap and heap[0][1] > w:
                    storage.append(heapq.heappop(heap))

                if not heap:
                    return w

                profit, capital = heapq.heappop(heap)
                # output += capital
                w -= profit
                k -= 1

                for stuff in storage:
                    heapq.heappush(heap, stuff)
            else:
                return w