class Solution:
    def countBits(self, n: int) -> list[int]:
        def hammingWeight(n: int) -> int:
            count = 0
            while n != 0:
                if n % 2 == 1:
                    count += 1
                n = n // 2

            return count

        ans = []

        for i in range(n+1):
            ans.append(hammingWeight(i))

        return ans