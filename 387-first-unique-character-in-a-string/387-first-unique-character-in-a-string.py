class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for i, ch in enumerate(s):
            if ch in counter:
                counter[ch][1] += 1
            else:
                counter[ch] = [i, 1]
        
        for key, value in counter.items():
            if value[1] == 1:   return value[0]
        
        return -1