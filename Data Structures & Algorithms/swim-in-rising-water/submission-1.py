class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        min_heap = [[grid[0][0], 0, 0]]
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if r == N-1 and c == N-1:
                return t

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newC < 0 or
                    newR == N or newC == N or
                    (newR, newC) in visited):
                    continue
                visited.add((newR, newC))
                heapq.heappush(min_heap, [max(t, grid[newR][newC]), newR, newC])