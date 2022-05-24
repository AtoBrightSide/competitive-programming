class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = [0] * len(s)
        
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == ")":
                stack.pop()
                if stack:   longest[i] = i - stack[-1]
                else:       stack.append(i)                    
            
            else:   stack.append(i)
                
        return max(longest) if len(s) != 0 else 0