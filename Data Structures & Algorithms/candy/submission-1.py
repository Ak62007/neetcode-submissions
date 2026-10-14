class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i]:
                candies[i] = candies[i-1] + 1

            elif ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                    candies[i-1] = candies[i] + 1

        # print(candies)
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i] and candies[i+1] >= candies[i]:
                candies[i] = candies[i+1] + 1

            elif ratings[i+1] > ratings[i] and candies[i+1] <= candies[i]:
                    candies[i+1] = candies[i] + 1


        # print(candies)
        return sum(candies)
