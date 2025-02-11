class Solution:
    def numberOfWays(self, s: str) -> int:
        s = [int(ch) for ch in s]
        
        ones = [ [ s[0], s[-1] ] for _ in range(len(s)) ]
        zero = [ [ 1 - s[0], 1 - s[-1] ] for _ in range(len(s)) ]
        for i in range(1, len(s)):
            ones[i][0] = ones[i - 1][0] + (1 if s[i] else 0)            
            zero[i][0] = zero[i - 1][0] + (1 if not s[i] else 0)
            
        for i in range(len(s) - 2, -1, -1):
            ones[i][1] = ones[i + 1][1] + (1 if s[i] else 0)
            zero[i][1] = zero[i + 1][1] + (1 if not s[i] else 0)
        
        ways = 0
        for i in range(1, len(s) - 1):
            if s[i]:
                if zero[i][0] > 0 and zero[i][1] > 0:
                    ways += zero[i][0] * zero[i][1]
            else:
                if ones[i][0] > 0 and ones[i][1] > 0:
                    ways += ones[i][0] * ones[i][1]
        
        return ways