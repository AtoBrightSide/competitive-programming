class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            md = l + (r - l)//2
            if nums[md] == target:
                return md
            if nums[md] > target:                
                if nums[md] != nums[0] and nums[md - 1] < target:
                    return md
                r = md - 1
            else:
                if nums[md] != nums[-1] and nums[md + 1] > target:
                    return md + 1
                l = md + 1
    
        return 0 if target < nums[0] else len(nums)