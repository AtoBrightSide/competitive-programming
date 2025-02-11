class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = left = right = 0
        for ch in s:
            if ch == '(':           left += 1
            else:                   right += 1
            
            if left == right:       longest = max(longest, 2 * right)
            elif right >= left:     left = right = 0
        
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':         left += 1
            else:                   right += 1
            
            if left == right:       longest = max(longest, 2 * left)
            elif left >= right:     left = right = 0
                
        return longest