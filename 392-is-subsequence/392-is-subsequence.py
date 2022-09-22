class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        
        for i, ch in enumerate(t):
            if ptr >= len(s):
                return True
            if ch == s[ptr]:
                ptr += 1
        
        return ptr == len(s)
    