class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        best_difference = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            bigger = max(nums[-1] - k, nums[i] + k)
            smaller = min(nums[0] + k, nums[i+1] - k)
            
            best_difference = min(best_difference, bigger - smaller)
        
        return best_difference