class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for p in range(len(prices) - 1):
            profit = max(prices[p+1:]) - prices[p]
            if profit > best:
                best = profit
        return best