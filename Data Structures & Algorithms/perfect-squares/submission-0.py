class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i**2 for i in range(1, int(n**0.5)+1)]
        q = deque()
        q.append((0, 0))
        output = 0

        cache = {0}
        while q:
            i, curr = q.popleft()
            for num in nums:
                if num + i == n:
                    return curr+1
                elif num + i < n:
                    if num+i not in cache:
                        cache.add(num+i)
                        q.append((num+i, curr+1))
