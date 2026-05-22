class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def isanagram(string1: str, string2: str) -> bool:
            return sorted(string1) == sorted(string2)
        
        mapping = []
        bool_map = [False]*len(strs)

        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if bool_map[j]:
                    continue
                else:
                    if isanagram(strs[i], strs[j]):
                        if not len(mapping)==0:
                            if strs[i] not in mapping[-1]:
                                mapping.append([strs[i], strs[j]])
                                bool_map[j] = True
                                bool_map[i] = True
                            else:
                                mapping[-1].append(strs[j])
                                bool_map[j] = True
                        else:
                            mapping.append([strs[i], strs[j]])
                            bool_map[j] = True
                            bool_map[i] = True
                    else:
                        continue
        for i in range(len(bool_map)):
            if not bool_map[i]:
                mapping.append([strs[i]])
        return mapping
    