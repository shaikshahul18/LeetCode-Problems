def maxProfit(prices):
    minPrice = prices[0]
    maxDiff = 0
    for price in prices:
        if price < minPrice:
            minPrice = price
        diff = price - minPrice

        if diff > maxDiff:
            maxDiff = diff
    return maxDiff
