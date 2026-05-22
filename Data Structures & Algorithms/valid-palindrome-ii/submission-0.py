class Solution:
    def validPalindrome(self, s: str) -> bool:
        def clean_str(string: str):
            return "".join(char for char in string if char.isalnum())

        def check_palindrom(string : str) -> bool:
            string = list(string)
            i = 0
            j = len(string) - 1
            
            while(i <= j):
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True

        s_set = set(s)

        if check_palindrom(s):
            return True
        else:
            for char in s_set:
                cs = s.replace(char, "")
                if check_palindrom(cs):
                    return True
                else:
                    continue
            
        return False