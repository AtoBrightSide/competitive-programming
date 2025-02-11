class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_tracker = [0] * 26
        for ch in s:
            idx = ord(ch) - 97
            s_tracker[idx] += 1
        
        t_tracker = [0] * 26
        for ch in t:
            idx = ord(ch) - 97
            t_tracker[idx] += 1
            
        
        return t_tracker == s_tracker