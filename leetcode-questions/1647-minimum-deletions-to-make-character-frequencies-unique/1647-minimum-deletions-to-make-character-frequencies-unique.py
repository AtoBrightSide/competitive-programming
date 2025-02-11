class Solution:
    def minDeletions(self, s: str) -> int:
        freq= Counter(s)
        freq, count = list(freq.values()), 0
        freq.sort()
        
        '''
        freq 
        curr 0
        count 6
        there 3 2 1
        '''    
        
        there = set()
        while freq:
            curr = freq.pop()
            while curr in there:
                count += 1
                curr -= 1
            if curr != 0:   there.add(curr)
                
        return count
