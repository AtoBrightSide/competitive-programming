class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) + 1):
            ans ^= i
            if i < len(nums):   ans ^= nums[i]
        
        return ans