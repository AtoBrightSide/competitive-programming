class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l,r = 1,max(time)*totalTrips
        while l<=r:
            md = l+(r-l)//2
            if self.myHelper(time, md) >= totalTrips:
                r = md-1
                best = md
            else:
                l = md+1
        return best
    def myHelper(self, time, sec):
        total = 0
        for t in time:
            if sec>=t:
                total += (sec//t)
        return total
