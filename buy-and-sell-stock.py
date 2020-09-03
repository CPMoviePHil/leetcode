def max_profit(prices):
    # 假如第一天購買是7塊
    # 第二天賣掉是1塊，獲利是-6塊
    # 這時就要拋棄第1天購買的想法，改在第2天購買
    # 為什麼呢?
    # 因為股票都是正數，就算後面天數價格有高於7塊的，但絕對比不過在跟第2天購買的價差
    # 假設第5天是10塊好了，第一天購買的獲利絕對會小於第2天購買
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