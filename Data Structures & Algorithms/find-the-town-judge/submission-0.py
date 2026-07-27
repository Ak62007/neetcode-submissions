class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = [i+1 for i in range(n)]
        track = {i+1:0 for i in range(n)}

        print(track)

        for t in trust:
            track[t[1]] += 1
            if t[0] in candidates:
                candidates.remove(t[0])

        if len(candidates) == 1 and track[candidates[0]] == n-1:
            return candidates[0]

        return -1

