class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        i = j = 0
        result = -1

        while j < len(s):
            hm[s[j]] = hm.get(s[j], 0) + 1
            
            while (j-i+1) - max(hm.values()) > k:
                hm[s[i]] -= 1
                i +=1
            
            result = max(j-i+1, result)

            j += 1

        return result