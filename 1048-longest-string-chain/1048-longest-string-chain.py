class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        mywords = set(words)
        memo = {}
        words.sort(key=lambda w:len(w), reverse=True)
        
        def dp(s):
            if len(s) == len(words[-1]): return 0
            if s in memo:   return memo[s]
            
            best = 0
            for i in range(len(s)):
                curr = s[:i] + s[i+1:]
                if curr in mywords:
                    best = max(1 + dp(curr), best)
            
            memo[s] = best
            return memo[s]
        
        ans = 0
        for word in words:
            memo[word] = 1 + dp(word)
            ans = max(ans, memo[word])
        
        return ans