class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        span = 1
        if self.prices:
            i = len(self.prices) - 1
            while i >= 0:
                if self.prices[i] <= price:
                    span += 1
                    i -= 1
                else:
                    break
        
        self.prices.append(price)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)