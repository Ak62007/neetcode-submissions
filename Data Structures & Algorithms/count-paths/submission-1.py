class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        track = [1]*n

        for i in range(1, m):
            for j in range(1, n):
                track[j] = track[j] + track[j-1]


        return track[-1]