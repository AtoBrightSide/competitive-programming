class Solution:
    def romanToInt(self, s: str) -> int:
        '''

        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        
        M C M X C I V
        
        1000 100 1000
        
        L V I I I
        
        50 + 5 + 1 + 1 + 1
        
        
        M C M C M X C 
        '''
        mapper = {"I":1, "X":10, "C":100, "M":1000, "D":500, "C":100, "L":50, "V":5}
        subs = {"I":["V","X"], "X":["L","C"], "C":["D","M"]}
        number = r = 0
        
        while r < len(s):
            curr = s[r]
            if r < len(s) - 1 and curr in subs:
                if s[r + 1] in subs[curr]:
                    number += mapper[s[r+1]] - mapper[curr]
                    r += 2
                    continue
            number += mapper[curr]
            r += 1
        return number