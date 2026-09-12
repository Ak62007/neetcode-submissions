class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        ROWS, COLS = len(heights), len(heights[0])
        visited = set()
        
        min_heap = [[0,0,0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while min_heap:
            diff, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue

            if (r, c) == (ROWS-1, COLS-1):
                return diff

            visited.add((r, c))
            
            for dr, dc in directions:
                newR, newC = r + dr, c + dc

                if (newR < 0 or newC < 0 or
                    newR == ROWS or newC == COLS or
                    (newR, newC) in visited):
                    continue

                new_diff = max(diff, abs(heights[r][c] - heights[newR][newC]))

                heapq.heappush(min_heap, [new_diff, newR, newC])