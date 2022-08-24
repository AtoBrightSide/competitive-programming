class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, sumSoFar):
            if i == len(nums):   return 1 if sumSoFar == target else 0
                
            if (i, sumSoFar) in memo:   return memo[(i, sumSoFar)]
            
            memo[(i, sumSoFar)] = dp(i+1, sumSoFar + nums[i]) + dp(i+1, sumSoFar - nums[i])
            return memo[(i, sumSoFar)]
        
        return dp(0, 0)