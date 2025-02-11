class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dp(i, stack):
            if i >= len(s):
                return stack == tuple([])
            
            if s[i] == "*":
                left = dp(i + 1, stack + tuple(["("]))
                right = False
                if stack:
                    right = dp(i + 1, stack[:-1])
                
                return left or right or dp(i + 1, stack)
            
            if s[i] == "(":
                return dp(i + 1, stack + tuple(["("]))
            elif stack:
                return dp(i + 1, stack[:-1])
            
            return False
        
        return dp(0, tuple([]))