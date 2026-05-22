class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = prices[0]
        min_idx = 0
        for i in range(1, len(prices)):
            # for a window
            if prices[i] < min_p:
                min_p = prices[i]
                min_idx = i
            if i == min_idx:
                continue
            if (prices[i] - min_p) > profit:
                profit = prices[i] - min_p
        return profit
    