class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:  return 0
        so_far = 1
        count = l = r = 0
        
        while r < len(nums):
            so_far *= nums[r]
            if so_far >= k:
                while so_far >= k and l <= r:
                    so_far /= nums[l]
                    l += 1
            count += (r - l + 1)
            r += 1
        
        return count