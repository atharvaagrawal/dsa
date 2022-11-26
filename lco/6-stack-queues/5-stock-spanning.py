# Stock Spanning
'''
Prices: 100  80  60  70  60  75  85
Spans:  1    1    1   2   1  4   6
'''

prices = [100, 80, 60, 70, 60, 75, 85]

spans = [1]

for i in range(1, len(prices)):
    j = i - 1
    if prices[i] < prices[j]:
        spans.append(1)
        continue
    else:
        while True:
            j = j - spans[j]
            if prices[i] < prices[j]:
                spans.append(i-j)
                break

print("Prices: ", prices)
print("Spans: ", spans)
