class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        matched = {}
        used = {}
        
        for ch in range(len(s)):
            if s[ch] in matched and matched[s[ch]] != t[ch]: 
                return False
                
            if t[ch] in used and used[t[ch]] != s[ch]:
                return False
            
            matched[s[ch]] = t[ch]
            used[t[ch]] = s[ch]
            
        return True