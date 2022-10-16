class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        if nums[-1] == 0:   return 0
        
        for i, num in enumerate(nums):
            if num != 0:
                l = i
                break
                
        so_far = 0
        ops = 0
        
        for i in range(l, len(nums)):
            nums[i] -= so_far
            if nums[i] > 0:
                so_far += nums[i]
                ops += 1
        
        return ops