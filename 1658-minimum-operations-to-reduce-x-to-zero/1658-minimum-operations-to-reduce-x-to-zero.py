class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = right = curr = 0
        required = sum(nums) - x
        ops = float('inf')
        
        if len(nums) == 1 and required == 0:
            return 1
        
        while required >= 0 and left <= right and right < len(nums):
            curr += nums[right]
            right += 1
            
            while left <= right and curr >= required:
                if curr == required:    ops = min(ops, len(nums) - (right - left))
                curr -= nums[left]
                left += 1
            
        return ops if ops != float('inf') else -1