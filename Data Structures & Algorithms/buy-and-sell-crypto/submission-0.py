class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        max_yet = prices[-1]

        for i in range(n-2, -1, -1):
            max_yet = max(max_yet, prices[i])
            max_profit = max(max_profit, max_yet - prices[i])
        
        return max_profit