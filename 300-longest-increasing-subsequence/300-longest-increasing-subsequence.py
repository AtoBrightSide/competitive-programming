class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        memo, longest = {len(nums) - 1: 1}, -1

        @lru_cache(None)
        def dfs(index):                
            longest = 1
            for i in range(index + 1, len(nums)):
                if nums[i] > nums[index]:   
                    longest = max(longest, 1 + dfs(i))

            return longest
        
        for i in range(len(nums)):
            longest = max(longest, dfs(i))
        return longest