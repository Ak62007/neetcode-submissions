class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        char_list = [(a, "a"), (b, "b"), (c, "c")]

        crt_list = []
        for cnt, char in char_list:
            if cnt != 0:
                crt_list.append([-cnt, char])

        heapq.heapify(crt_list)
        res = ""

        while crt_list:
            count, char = heapq.heappop(crt_list)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not crt_list:
                    break
                count2, char2 = heapq.heappop(crt_list)
                res += char2
                count2 += 1

                if count2:
                    heapq.heappush(crt_list, [count2, char2])

            else:
                res += char
                count += 1
            if count:
                heapq.heappush(crt_list, [count, char])

        return res
        