def maxProfit(prices: list) -> int:
    min_price = prices[0]
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i]-min_price
    return max_profit


prices = [1, 16, 15, 14, 16, 14, 100]
p = maxProfit(prices)
print(p)