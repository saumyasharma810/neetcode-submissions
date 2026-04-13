class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftMax = [-1] * len(prices)
        for i in range(len(prices)-2,-1,-1):
            leftMax[i] = max(leftMax[i+1],prices[i+1])
        maxProfit = 0
        for i, price in enumerate(prices):
            maxProfit = max(maxProfit, leftMax[i]-price)
        return maxProfit
        