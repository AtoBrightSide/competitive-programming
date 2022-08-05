class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:      
        dp = [0] * (target + 1)
        dp[0] = 1
        nums.sort()
        
        for i in range(1, target + 1):
            for j in range(len(nums)):
                curr = i - nums[j]
                if curr < 0:    break
                dp[i] += dp[curr]
        
        return dp[-1]