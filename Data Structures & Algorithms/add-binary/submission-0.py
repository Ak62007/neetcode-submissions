class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        answer = []

        n = a + b
        if n == 0:
            return "0"
        while n != 0:
            answer.append(str(n % 2))
            n = n // 2

        return "".join(answer[::-1])