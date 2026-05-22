class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        lent = min([len(word1), len(word2)])
        i = 0

        while(i < lent):
            ans += word1[i] + word2[i]
            i += 1

        if len(word1) > len(word2):
            ans = ans + word1[lent:len(word1)]
            return ans
        elif len(word2) > len(word1):
            ans = ans + word2[lent:len(word2)]
            return ans
        else:
            return ans            