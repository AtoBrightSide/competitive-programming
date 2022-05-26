class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        memo, longest = {len(nums) - 1: 1}, -1

        for i in range(len(nums)):
            longest = max(longest, self.dfs(i, nums, memo))
        
        return longest
            
    def dfs(self, index, nums, memo):        
        if index in memo:   
            return memo[index]
        
        longest = 1
        for i in range(index + 1, len(nums)):
            if nums[i] > nums[index]:   
                longest = max(longest, 1 + self.dfs(i, nums, memo))
        
        memo[index] = longest
        return memo[index]