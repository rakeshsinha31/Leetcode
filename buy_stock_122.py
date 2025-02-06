def maxProfit(prices: list) -> int:
    idx = 0
    max = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit = prices[i] - prices[i-1]
            max += profit

    return max



prices = [7,2,5,33,1]
p = maxProfit(prices)
print(p)