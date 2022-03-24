"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
#         O(nlogn)
        res,ans = [],[]
        for x in range(1,1001):
            if self.mySearch(x, z, customfunction) == []:
                continue
            res.append(self.mySearch(x, z, customfunction))
        ans = [l for l in res if l!=None and len(l) > 0]
        return ans
    def mySearch(self, x, z, customfunction):
        l,r=1,1000
        while l<=r:
            m = (l+r)//2
            if customfunction.f(x, m) > z:
                r = m - 1
            elif customfunction.f(x, m) < z:
                l = m + 1
            else:
                return [x,m]
        return 
        
