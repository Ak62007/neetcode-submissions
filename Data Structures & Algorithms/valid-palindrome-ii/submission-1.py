class Solution:
    def validPalindrome(self, s: str) -> bool:
        def clean_str(string: str):
            return "".join(char for char in string if char.isalnum())

        def ifpalin(s:str):
            if s==s[::-1]:
                return True
            else:
                return False
        
        if ifpalin(s):
            return True
        else:
            i = 0
            j = len(s) - 1
            while(i <= j):
                if s[i] != s[j]:
                    if not (s[i+1] == s[j] or s[i] == s[j-1]):
                        return False
                    else:
                        if ifpalin(s[i+1:j+1]) or ifpalin(s[i:j]):
                            return True
                        else:
                            return False
                i += 1
                j -= 1