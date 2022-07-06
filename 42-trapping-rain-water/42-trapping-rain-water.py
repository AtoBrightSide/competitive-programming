class Solution:
    def trap(self, height: List[int]) -> int:
        tracker = defaultdict(lambda: [float(inf), float(inf)])
        lmax = rmax = -float(inf)
        for i, num in enumerate(height):
            tracker[i][0] = lmax
            lmax = max(lmax, num)
        for i in range(len(height)-1, -1, -1):
            tracker[i][1] = rmax
            rmax = max(rmax, height[i])
        
        trapped = 0
        for i, val in tracker.items():
            curr = min(val)
            if i != 0 and i != len(height) - 1 and curr > height[i]:
                trapped += (curr - height[i])
                
        return trapped