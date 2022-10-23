class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float("inf")
        curr_window = r = 0
        
        for l in range(len(nums)):
            while r < len(nums) and curr_window < target:
                curr_window += nums[r]   
                r += 1
            
            if curr_window >= target:  
                best = min(best, r - l)
            curr_window -= nums[l]
        
        if best == float("inf"):
            return 0
        
        return best