class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        bought = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > bought:
                maxProfit = max(prices[i]-bought, maxProfit)
            else:
                bought = prices[i]
        return maxProfit
