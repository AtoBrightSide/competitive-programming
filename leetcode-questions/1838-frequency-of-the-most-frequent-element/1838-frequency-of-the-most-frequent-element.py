class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        prefix = [num for num in nums]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        
        window = 1
        r = 0
        for l, num in enumerate(nums):
            while r < len(nums) and l < len(nums) and abs(num * (r - l + 1) - (prefix[r] - (prefix[l-1] if l > 0 else 0))) <= k:
                r += 1
            
            window = max(window, r - l)
        
        return window