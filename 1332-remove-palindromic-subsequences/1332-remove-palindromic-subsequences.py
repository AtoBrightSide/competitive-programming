class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0: return 0
        
        return 1 if s == s[::-1] else 2
        