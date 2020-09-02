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
            elif profit > 0 and profit < prices[counter] + buy:
                profit = prices[counter] + buy
        counter += 1
    return profit



print(max_profit([1,2,4]))