class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        
        longest, flag = 0, False
        for ch, freq in counter.items():
            if freq % 2 == 0:   longest += freq
            else:   
                longest += (freq - 1)
                flag = True
        
        return longest + (1 if flag else 0)