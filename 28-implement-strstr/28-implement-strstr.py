class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, len(needle) - 1
        haystack, needle = list(haystack), list(needle)
        
        while r < len(haystack):
            if haystack[l:r+1] == needle:  return l
            l += 1
            r += 1
            
            
        return -1 if needle != [] else 0
        
            