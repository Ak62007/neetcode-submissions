class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1] + 1
            # elif ratings[i-1] == ratings[i]:
            #     candies[i], candies[i-1] = max(candies[i], candies[i-1]), max(candies[i], candies[i-1])
            elif ratings[i-1] > ratings[i]:
                if candies[i-1] <= candies[i]:
                    candies[i-1] = candies[i] + 1
                j = i - 1
                while ratings[j-1] > ratings[j] and j > 0:
                    if candies[j-1] <= candies[j]:
                        candies[j-1] = candies[j] + 1
                    j -= 1

        print(candies)
        return sum(candies)
