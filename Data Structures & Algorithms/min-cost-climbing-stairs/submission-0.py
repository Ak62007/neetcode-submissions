class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Solving using Tabulation
        # cost.append(0)
        last_last = cost[0]
        last = cost[1]

        for i in range(2, len(cost)):
            last, last_last = min(last, last_last) + cost[i], last

        return min(last, last_last)