class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distances.append([(x**2 + y**2)**0.5, [x, y]])

        heapq.heapify(distances)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(distances)[1])

        return res