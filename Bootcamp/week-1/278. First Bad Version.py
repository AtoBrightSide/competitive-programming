# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution: 
    def firstBadVersion(self, n: int) -> int:
        l,r = 0, n
        while l<=r:
            md = (l+r)//2
            if isBadVersion(md):
                r = md - 1
                best = md
            elif not isBadVersion(md):
                l = md + 1
        return best
        
                
