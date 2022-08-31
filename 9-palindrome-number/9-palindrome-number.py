class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:   return False
        L = len(str(x))
        x = str(x)
        for i in range(L // 2):
            if x[i] != x[L-1-i]:    return False
        return True