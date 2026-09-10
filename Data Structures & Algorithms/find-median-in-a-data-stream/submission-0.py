class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap and self.min_heap:
            if num > -self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)

        elif self.max_heap or self.min_heap:
            if self.max_heap:
                if num > -self.max_heap[0]:
                    heapq.heappush(self.min_heap, num)
                else:
                    heapq.heappush(self.max_heap, -num)
            else:
                if num < self.min_heap[0]:
                    heapq.heappush(self.max_heap, -num)
                else:
                    heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, num)

        elif len(self.min_heap) > len(self.max_heap):
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if self.max_heap and self.min_heap:
            if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
                return (-self.max_heap[0] + self.min_heap[0]) / 2
            else:
                if len(self.max_heap) > len(self.min_heap):
                    return -self.max_heap[0]
                else:
                    return self.min_heap[0]

        elif self.max_heap or self.min_heap:
            if self.min_heap:
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()