# from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        elif s.strip() == "":
            return 1

        mapping = {}
        seq = set()
        max_len = 0
        for i, letter in enumerate(s):
            if letter not in seq:
                mapping[letter] = i
                seq.add(letter)
                # if letter in seq:
                #     if len(seq) > max_len:
                #         max_len = len(seq)
                #     seq = set(mapping.keys())
                # else:
                #     seq.add(letter)
            else:
                if len(seq) > max_len:
                    max_len = len(seq)
                seq = set(s[mapping[letter]+1:i+1])
                mapping[letter] = i

        if len(seq) > max_len:
            max_len = len(seq)

        return max_len

