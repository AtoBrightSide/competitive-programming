class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # for i in range(len(nums)):
        #     min_index = i
        #     for j in range(i+1, len(nums)):
        #         if nums[j] < nums[min_index]:   min_index = j
        #     nums[min_index], nums[i] = nums[i], nums[min_index]
        
        count = [0,0,0]
        for num in nums:
            if num == 0:    count[0] += 1
            if num == 1:    count[1] += 1
            if num == 2:    count[2] += 1
        
        i = 0
        while count[0]:
            nums[i] = 0
            i += 1
            count[0] -= 1
        while count[1]:
            nums[i] = 1
            i += 1
            count[1] -= 1
        while count[2]:
            nums[i] = 2
            i += 1
            count[2] -= 1
            