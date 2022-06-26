class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        left, right = 0, 1
        while right < len(nums):
            if nums[left] > nums[right]:
                count += 1
                if count > 1:   return False
                if left > 0 and right < len(nums)-1:
                    if nums[left - 1] > nums[right] and nums[right + 1] < nums[left]:   return False
                
                elif right < len(nums)-1 and nums[right] > nums[right + 1]: return False
            
            left += 1
            right += 1
            
        return count < 2