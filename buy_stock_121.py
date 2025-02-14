def maxProfit(prices: list) -> int:
    l=0
    r=1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit

prices = [108, 16, 15, 14, 16, 149, 100]
p = maxProfit(prices)
print(p)