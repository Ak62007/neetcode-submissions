class StockSpanner:

    def __init__(self):
        self.prices = []
        self.cur_idx = -1

    def next(self, price: int) -> int:
        self.cur_idx += 1
        while self.prices and self.prices[-1][1] <= price:
            self.prices.pop()

        if self.prices:
            span = self.cur_idx - self.prices[-1][0]
            self.prices.append((self.cur_idx, price))
            return span
        else:
            if self.cur_idx == 0:
                self.prices.append((self.cur_idx, price))
                return 1
            else:
                self.prices.append((self.cur_idx, price))
                return self.cur_idx + 1