class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        L = len(p)
        N = len(s)
        anagrams = []
        if L > N:
            return anagrams
        
        window_map = Counter(s[:L])
        p_map = Counter(p)
        
        start, end = 0, L
        while end < len(s):
            if window_map == p_map:
                anagrams.append(start)
                
            if window_map[s[start]] == 1:
                del window_map[s[start]]
            else:
                window_map[s[start]] -= 1
            
            window_map[s[end]] = window_map.get(s[end], 0) + 1
            
            start += 1
            end += 1
        
        if window_map == p_map:
            anagrams.append(start)
        
        return anagrams