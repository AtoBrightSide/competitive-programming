class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx, d = 0, {}
        for i in range(len(prices)):
            curr = self.dp(i, prices, d) - prices[i]
            if curr > mx:
                mx = curr
        return mx

    def dp(self, i, prices, d):
        if i == len(prices)-1:
            return prices[i]
        if i in d:
            return d[i]
        
        res = max(prices[i], self.dp(i+1, prices, d))
        d[i] = res
        
        return res
