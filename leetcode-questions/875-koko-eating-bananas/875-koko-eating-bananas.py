class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / k)
            return hrs
        
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            
            if canEat(mid) > h:     l = mid + 1
            else:                   r = mid - 1
        
        return l