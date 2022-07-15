class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, nums = 1, set(nums)
        
        while i in nums:
            i += 1
        return i
        
        