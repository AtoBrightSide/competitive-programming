class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        slow = fast = 0
        
        while fast < len(nums):
            while fast < len(nums) and nums[fast] == 0:
                fast += 1
            if slow <= fast < len(nums):
                nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast += 1