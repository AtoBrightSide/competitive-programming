class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)-2, -1, -1):
            if prices[i] < prices[i+1]:
                best = max(best, prices[i+1] - prices[i])
                prices[i] = prices[i+1]
        return best