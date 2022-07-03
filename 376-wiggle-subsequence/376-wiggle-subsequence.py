class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, isUp):
            if i == len(nums) - 1:  return 1
            
            if (i, isUp) in memo:   return memo[(i, isUp)]
            
            count = 1
            for j in range(i+1,len(nums)):
                if isUp:
                    if nums[i] < nums[j]:   count = max(count, 1 + dp(j, not isUp))
                else:
                    if nums[i] > nums[j]:   count = max(count, 1 + dp(j, not isUp))
                    
            memo[(i, isUp)] = count
            return memo[(i, isUp)]
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dp(i, True), dp(i, False))
        
        return ans