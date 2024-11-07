def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 1:
        return 0

    buy = prices[0]
    index = 0
    leng = len(prices)
    for i in range(leng):
        if prices[i] <= buy:
            buy = prices[i]
            index = i
            index += 1
            if prices[i] == prices[-1]:
                return 0

    sell = buy
    profit = 0
    for i in range(index, len(prices)):
        if (prices[i]-buy) > sell:
            sell = (prices[i]-buy)
    return sell
    
prices = [3,3]
print(maxProfit(prices))