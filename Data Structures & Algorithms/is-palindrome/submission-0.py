class Solution:
    def isPalindrome(self, s: str) -> bool:
        def clean_alphanumeric(text):
            return ''.join(char for char in text if char.isalnum())

        def reverse_s(string: str) -> str:
            string = list(string)
            i = 0
            j = len(string) - 1

            while(i <= j):
                temp = string[i]
                string[i] = string[j]
                string[j] = temp
                i += 1
                j -= 1
            return "".join(string)

        s = s.lower()
        clean_s = clean_alphanumeric(s)
        if reverse_s(clean_s) == clean_s:
            return True
        else:
            return False