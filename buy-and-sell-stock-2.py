def max_profit_2(prices):
    # 假如第一天購買是7塊
    # 第二天賣掉是1塊，獲利是-6塊
    # 這時就要拋棄第1天購買的想法，改在第2天購買
    # 為什麼呢?
    # 因為股票都是正數，就算後面天數價格有高於7塊的，但絕對比不過在跟第2天購買的價差
    # 假設第5天是10塊好了，第一天購買的獲利絕對會小於第2天購買
    profits = []
    buy = prices[0]
    counter = 1
    while counter < len(prices):
        if prices[counter] < buy:  # 要記住一點就是，只要遇到更低的購買價格就要收購，因為後面出現了更高價一定會有更多獲利
            buy = prices[counter]
        else:
            profits.append(prices[counter] - buy)
            buy = prices[counter]  # 因為可以當天賣，也可以當天買該價格
        counter += 1
    return sum(profits)

print(max_profit_2([7,1,5,3,10,4]))