class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = 0
        for i, num in enumerate(nums):
            if num <= 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
        
        for i in range(count, len(nums)):
            curr = abs(nums[i]) + count - 1
            if curr < len(nums):    
                nums[curr] *= -1 if nums[curr] > 0 else 1
        
        for i, num in enumerate(nums):
            if num > 0: return i + 1 - count
        
        return len(nums) + 1 - (count if count else 0)