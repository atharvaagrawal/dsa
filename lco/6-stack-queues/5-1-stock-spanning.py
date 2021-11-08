# Stock Spanning
'''
Prices: 100  80  60  70  60  75  85
Spans:  1    1    1   2   1  4   6
'''


class StockSpanner:
    def __init__(self):
        self.prices = []
        self.spans = []

    def __str__(self):
        return "Prices: " + str(self.prices) + "\n\n Span: " + str(self.spans)

    def calculateSpan(self, price):
        index = len(self.prices) - 1

        while index >= 0 and self.prices[index] <= price:
            span = self.spans[index]
            index = index - span

        self.prices.append(price)
        element_index = len(self.prices) - 1
        span = element_index - index
        self.spans.append(span)


sp = StockSpanner()
sp.calculateSpan(100)
sp.calculateSpan(80)
sp.calculateSpan(60)
sp.calculateSpan(70)
sp.calculateSpan(60)
sp.calculateSpan(75)
sp.calculateSpan(85)
print(sp)
