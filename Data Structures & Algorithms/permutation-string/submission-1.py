class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        truth_dict = {}
        for l in s1:
            truth_dict[l] = truth_dict.get(l, 0) + 1

        i = 0
        j = len(s1) - 1

        while j < len(s2):
            ss = s2[i:j+1]
            check_dict = {}
            for l in ss:
                check_dict[l] = check_dict.get(l, 0) + 1
            
            flag = True
            for key, value in check_dict.items():
                if truth_dict.get(key) == None:
                    flag = False
                    break
                else:
                    if truth_dict[key] == value:
                        continue
                    else:
                        flag = False
            
            if flag == True:
                return True
            else:
                i += 1
                j += 1
                continue

        return False