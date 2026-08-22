class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        cache = set()
        def is_palim(string):
            if len(string) == 1:
                return True

            i, j = 0, len(string)-1

            while i < j:
                if string[i] == string[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            
            return True

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in cache:
                    count += 1
                elif is_palim(s[i:j+1]):
                    count += 1
                    cache.add(s[i:j+1])

        return count
