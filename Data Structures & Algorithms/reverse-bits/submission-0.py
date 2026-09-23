class Solution:
    def reverseBits(self, n: int) -> int:
        answer = ["0"]*32
        i = len(answer) - 1
        while n != 0:
            answer[i] = str(n % 2)
            n = n // 2
            i -= 1

        return int("".join(answer[::-1]), 2)