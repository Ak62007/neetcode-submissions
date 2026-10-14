class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        char_map = {}

        for l in s:
            char_map[l] = char_map.get(l, 0) + 1

        print(char_map)

        ans = []
        char_set = set()
        length = 0
        for i, l in enumerate(s):
            if l not in char_set:
                char_set.add(l)

            char_map[l] -= 1
            length += 1
            if not char_map[l]:
                char_set.remove(l)
                if not char_set:
                    ans.append(length)
                    length = 0

        return ans