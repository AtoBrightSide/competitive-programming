class Solution:
    def maxArea(self, height: List[int]) -> int:
        right, left = 0, len(height)-1
        mx = min(height[right], height[left]) * (left-right)
        while right<left:
            if height[right] > height[left]:
                left -= 1
            elif height[right] < height[left]:
                right += 1
            else:
                left -= 1
                right += 1
            mx = max(mx, min(height[right], height[left]) * (left-right))
            
        return mx