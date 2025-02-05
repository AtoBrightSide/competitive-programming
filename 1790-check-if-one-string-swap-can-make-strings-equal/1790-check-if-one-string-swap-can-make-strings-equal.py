class Solution:
    def freqCount(self, s):
        counter = {}
        for index in range(len(s)):
            currLetter = s[index]
            counter[currLetter] = counter.get(currLetter, 0) + 1
        return counter

    def areAlmostEqual(self, s1: str, s2: str) -> bool:    
        if self.freqCount(s1) != self.freqCount(s2):  
            return False
        
        count = 0
        for index in range(len(s1)):
            count += 1 if s1[index] != s2[index] else 0
        
        return count == 0 or count == 2