'''
Buy at low price and Sell at high price
'''

values = [int(x) for x in input().split()]


def maxSell(values):

    global_small = values[0]
    global_profit = 0  # System min values

    for value in values:
        global_small = min(global_small, value)

        current_profit = value - global_small

        global_profit = max(global_profit, current_profit)

    return ['global_small:', global_small, 'global_profit:', global_profit]


print(maxSell(values))
