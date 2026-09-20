class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        order = defaultdict(list)

        for word in words:
            for ch in word:
                order[ch]

        for i in range(len(words)-1):
            j, k = 0, 0
            s1, s2 = words[i], words[i+1]
            while j < len(s1) and k < len(s2):
                if s1[j] == s2[k]:
                    j += 1
                    k += 1
                    continue
                else:
                    order[s1[j]].append(s2[k])
                    break

            if k == len(s2) and len(s1) > len(s2):
                return ""
        
        visited = set()
        path = set()
        result = []
        def dfs(ch):
            if ch in visited:
                return True

            if ch in path:
                return False

            path.add(ch)

            for nei in order[ch]:
                if not dfs(nei):
                    return False

            path.remove(ch)
            visited.add(ch)
            result.append(ch)
            return True

        for key in order:
            if not dfs(key):
                return ""

        return "".join(result[::-1])