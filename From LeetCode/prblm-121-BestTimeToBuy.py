def maxProfit(prices):
    left = 0
    right = 1
    max_profit = 0
    while (right < len(prices)):
        profit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
