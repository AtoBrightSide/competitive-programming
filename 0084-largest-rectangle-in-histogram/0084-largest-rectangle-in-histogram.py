class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        
        ans = 0
        stack = [[heights[0], 0]]
        for i in range(1, len(heights)):
            curr = heights[i]
            flag = False
            while stack and stack[-1][0] > curr:
                curr_rect = stack.pop()
                ans = max(ans, curr_rect[0] * (i - curr_rect[1]))
                flag = True
            stack.append([curr, curr_rect[1] if flag else i])
            
        return ans