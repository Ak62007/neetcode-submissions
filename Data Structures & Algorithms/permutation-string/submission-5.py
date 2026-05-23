class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        truth_dict = {}
        check_dict = {}
        matches = 0
        for l in range(ord("a"), ord("z")+1):
            truth_dict[chr(l)] = 0
            check_dict[chr(l)] = 0

        for l in s1:
            truth_dict[l] += 1

        # print(f"Truth: {truth_dict}")

        i = 0
        j = len(s1) - 1

        # getting the initial matches
        for l in s2[i:j+1]:
            check_dict[l] += 1

        # print(f"Check: {check_dict}")

        for k in truth_dict.keys():
            if truth_dict[k] == check_dict[k]:
                matches += 1

        if matches == 26:
            return True

        # print(matches)

        i+=1
        j+=1

        while j < len(s2):
            left_char = s2[i - 1]
            right_char = s2[j]

            # remove left char
            if check_dict[left_char] == truth_dict[left_char]:
                matches -= 1

            check_dict[left_char] -= 1

            if check_dict[left_char] == truth_dict[left_char]:
                matches += 1


            # add right char
            if check_dict[right_char] == truth_dict[right_char]:
                matches -= 1

            check_dict[right_char] += 1

            if check_dict[right_char] == truth_dict[right_char]:
                matches += 1

            if matches == 26:
                return True
            else: 
                i += 1
                j += 1
                continue

        if matches == 26:
            return True
        else:
            return False

        
