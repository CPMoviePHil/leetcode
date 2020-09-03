def max_profit(prices):
    profit = 0
    counter = 1
    buy = -1 * prices[0]
    while counter < len(prices):
        if buy + prices[counter] < 0:
            buy = -1 * prices[counter]
        else:
            if profit == 0:
                profit = prices[counter] + buy
            elif 0 < profit < prices[counter] + buy:
                profit = prices[counter] + buy
        counter += 1
    return profit


def max_profit_2(prices):
    profit = 0
    for index, buy in enumerate(prices):
        for sell in prices[index:]:
            if sell - buy > 0:
                profit = max(profit, sell - buy)
    return profit

print(max_profit([1,2,4]))
print(max_profit_2([1,2,4]))