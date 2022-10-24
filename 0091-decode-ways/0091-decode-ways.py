class Solution:
    def numDecodings(self, s: str) -> int:
        mapper = {str(i):chr(i+96) for i in range(1, 27)}
        
        @cache
        def dp(i):
            if i >= len(s):     return 1
            if s[i] == '0':     return 0
            
            curr = dp(i+1)
            if i < len(s) - 1 and (str(s[i]) + str(s[i + 1])) in mapper:
                curr += dp(i+2)
            
            return curr
        
        return dp(0)