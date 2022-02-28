class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans=0
        for row in grid:
            ans += self.myBS(row)
        return ans
    
    def myBS(self, lst):
        l, r, best = 0, len(lst)-1, len(lst)
        while l<=r:
#           md = (l+r)//2
#           the below one covers everything
            md = l + (r-l)//2
            if lst[md] < 0:
                r = md-1
                best = md
            else:
                l = md + 1

        return len(lst)-best
