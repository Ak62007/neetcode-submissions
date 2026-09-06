class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            # pop the largest
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            # collide them
            res = first - second
            if res > 0:
                heapq.heappush(stones, -res)

        if len(stones) == 1:
            return -stones[0]
        else:
            return 0