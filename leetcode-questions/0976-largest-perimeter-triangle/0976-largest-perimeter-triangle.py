class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        curr = 0
        for i in range(2, len(nums)):
            if nums[curr] - nums[curr + 1] < nums[i]:
                return nums[curr] + nums[curr + 1] + nums[i]
            
            curr += 1
        
        return 0 