class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        vis = set()
        @cache
        def dfs(i):
            if i in vis:    return 0
            vis.add(i)
            curr = 1 + dfs(nums[i])
            return curr
        
        longest = 0
        for i, num in enumerate(nums):
            longest = max(longest, dfs(i))
        
        return longest