class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hashed = set(nums)
        
        ans = 0
        for num in nums:
            if num - 1 not in nums_hashed:
                curr = num + 1
                while curr in nums_hashed:
                    curr += 1
                ans = max(ans, curr - num)
            
        return ans