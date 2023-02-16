class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(nums):
                return 0
            
            rob = nums[i] + dp(i + 2)
            dont_rob = dp(i + 1)
            
            return max(rob, dont_rob)
        
        return dp(0)