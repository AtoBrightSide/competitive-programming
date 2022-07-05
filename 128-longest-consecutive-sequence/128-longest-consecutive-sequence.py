class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hashed = set(nums)
        memo = {}
        
        def dp(num):
            if num not in nums_hashed:  return 0
            
            if num in memo: return memo[num]
            
            memo[num] = 1 + dp(num+1)
            
            return memo[num]
        
        ans = 0
        for num in nums:
            ans = max(ans, dp(num))
            
        return ans