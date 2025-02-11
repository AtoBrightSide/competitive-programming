class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(nums):  return -float("inf")
            
            return max(nums[i], nums[i] + dp(i+1))
        
        ans = -float("inf") 
        for i in range(len(nums)):
            ans = max(ans, dp(i))
        
        return ans