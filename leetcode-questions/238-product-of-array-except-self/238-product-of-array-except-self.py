class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [num for num in nums]
        suffix = [num for num in nums]
        
        L = len(nums) - 1
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
            suffix[L-i] = suffix[L-i+1] * nums[L-i]
        
        res = [0] * len(nums)
        res[0], res[-1] = suffix[1], prefix[-2]
        
        for i in range(1, len(nums)-1):
            res[i] = (prefix[i-1] * suffix[i+1])
            
        return res