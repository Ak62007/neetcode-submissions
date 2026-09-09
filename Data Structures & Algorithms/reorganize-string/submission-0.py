class Solution:
    def reorganizeString(self, s: str) -> str:
        char_map = {}

        for l in s:
            char_map[l] = char_map.get(l, 0) + 1

        char_heap = []

        for char, cnt in char_map.items():
            char_heap.append([-cnt, char])

        heapq.heapify(char_heap)
        prev = None
        res = ""
        while char_heap or prev:
            if prev and not char_heap:
                return ""

            cnt, char = heapq.heappop(char_heap)
            cnt += 1
            res += char

            if prev:
                heapq.heappush(char_heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res
