class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:   return False
        tracker = [float("inf")] * len(nums)
        def bs(num):
            l, r = 0, len(nums) - 1
            
            while l <= r:
                md = l + (r - l) // 2
                
                if tracker[md] >= num:
                    r = md - 1
                else:
                    l = md + 1
            
            tracker[l] = num
        
        for num in nums:    bs(num)
        
        return tracker[2] != float("inf")