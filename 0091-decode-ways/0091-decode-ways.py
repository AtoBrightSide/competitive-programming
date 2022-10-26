class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [1 if ch != '0' else 0 for ch in s]
        dp.append(1)
        for i in range(len(s) - 2, -1, -1):
            if dp[i] != 0:
                if 1 <= int(s[i:i+2]) <= 26:
                    dp[i] = dp[i+1] + (dp[i+2] if (i + 2) < len(s) else 1)
                else:
                    dp[i] = dp[i+1]
        
        return dp[0]
        
    
    