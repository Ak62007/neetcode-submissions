from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def compare(s: str, t: str):
            common_str = ""
            if len(s) < len(t):
                for i in range(len(s)):
                    print("I am here upper loop")
                    if s[i] == t[i]:
                        common_str += s[i]
                    else:
                        print("I returned up")
                        return common_str
            else:
                for i in range(len(t)):
                    print("i am here down")
                    if t[i] == s[i]:
                        common_str += t[i]
                    else:
                        print("I returned down")
                        return common_str
            return common_str

        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 2:
            return compare(strs[0], strs[1])
        else:
            common_str = compare(strs[0], strs[1])
            print(common_str)
            for i in range(2, len(strs)):
                common_str = compare(common_str, strs[i])
                print(common_str)
            return common_str  