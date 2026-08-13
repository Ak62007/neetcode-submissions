class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        grid = [[False]*n for _ in range(n)]

        max_len = 1
        start = 0
        for i in range(n):
            grid[i][i] = True

        for ss_len in range(2, n+1):
            for i in range(n-ss_len+1):
                j = ss_len + i - 1

                if s[i] == s[j]:
                    if ss_len <= 3 or grid[i+1][j-1]:
                        grid[i][j] = True

                        if j-i+1 > max_len:
                            start = i
                            max_len = j-i+1

        return s[start:start+max_len]
