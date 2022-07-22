class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            curr = i+1
            if nums[i] < nums[curr]:
                while curr < len(nums) and nums[i] < nums[curr]:
                    curr += 1
                nums[i], nums[curr-1] = nums[curr-1], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return
        
        L = len(nums)-1
        for i in range(len(nums)//2):
            nums[i], nums[L-i] = nums[L-i], nums[i]