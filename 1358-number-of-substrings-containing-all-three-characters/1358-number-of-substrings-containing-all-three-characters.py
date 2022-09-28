class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = defaultdict(int)
        
        num = l = r = 0
        while l < len(s):
            while r < len(s) and len(freq) < 3:
                freq[s[r]] += 1
                r += 1
            
            if len(freq) == 3:  num += 1 + (len(s) - r)
            
            freq[s[l]] -= 1
            if freq[s[l]] <= 0:     del freq[s[l]]
            
            l += 1
        
        return num