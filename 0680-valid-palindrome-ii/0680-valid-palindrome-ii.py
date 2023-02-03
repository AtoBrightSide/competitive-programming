class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                delete_left = list(s[l + 1:r + 1]) == list(reversed(s[l + 1: r + 1]))
                delete_right = list(s[l:r]) == list(reversed(s[l:r]))
                
                return (False if (not delete_left and not delete_right) else True)
        
            l += 1
            r -= 1
        
        return True
    