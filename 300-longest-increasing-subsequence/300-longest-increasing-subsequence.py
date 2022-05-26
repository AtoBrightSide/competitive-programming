class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        dp = [1] * len(nums)
        
        for i in range(len(nums)-2, -1, -1):
            for j in range(i, len(nums)):
                dp[i] = max(dp[i], 1 + dp[j]) if nums[i] < nums[j] else dp[i]
        
        return max(dp)