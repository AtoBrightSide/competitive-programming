class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums [fast] == 0:    fast += 1
            else:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1
                slow += 1