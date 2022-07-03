class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        right, left, count = 1, 0, len(prices)
        
        while right < len(prices):
            while right < len(prices) and prices[right] + (right - left) == prices[left]:
                right += 1
            curr = right - left
            count += (curr * (curr-1))/2
            left = right
            right += 1
            
        return int(count)