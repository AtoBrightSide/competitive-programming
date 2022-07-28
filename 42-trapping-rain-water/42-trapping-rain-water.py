class Solution:
    def trap(self, height: List[int]) -> int:
        # highest from left and right
        L = len(height)-1
        left_high, right_high = [0] * (L+1), [0] * (L+1)
        for i in range(1, len(height)):
            left_high[i] = max(left_high[i-1], height[i-1])
            right_high[L-i] = max(right_high[L-i+1], height[L-i+1])
        
        trapped = 0
        for i, h in enumerate(height):
            curr = min(left_high[i], right_high[i])
            trapped += curr - (h if h < curr else curr)
            
        return trapped