class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr = [0] * 101
        for num in nums:
            arr[num] += 1
        
        nums = []
        for i, val in enumerate(arr):
            if val > 0: nums.extend([i] * 4)
        
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