class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        true_map = {}
        window_map = {}
        for l in t:
            true_map[l] = true_map.get(l, 0) + 1
            if l not in window_map.keys():
                window_map[l] = 0
            else:
                continue

        # print(true_map)
        # print(window_map)
        
        i, j = 0,0
        min_len = (len(s), (i,j))
        have, need = 0, len(true_map.keys())

        while j < len(s):
            if true_map.get(s[j]) is not None:
                window_map[s[j]] += 1
                print(window_map)
                if window_map[s[j]] == true_map[s[j]]:
                    have += 1
            
            j += 1

            while have == need:
                if min_len[0] >= (j-i):
                    min_len = (j-i, (i, j))
                if true_map.get(s[i]) is not None:
                    window_map[s[i]] -= 1
                    if window_map[s[i]] < true_map[s[i]]:
                        have -= 1

                i += 1

        # if min_len[0] >= (j-i+1):
        #     min_len = (j-i+1, (i, j))

        return s[min_len[1][0]: min_len[1][1]]
