class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for num in nums:
            if num == 0:    count[0] += 1
            if num == 1:    count[1] += 1
            if num == 2:    count[2] += 1
        
        i = 0
        for ind, val in enumerate(count):
            for _ in range(val):
                nums[i] = ind
                i += 1