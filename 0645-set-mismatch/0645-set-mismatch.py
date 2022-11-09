class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0: 
                ans.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1
        
        for i, num in enumerate(nums):
            if num > 0: 
                ans.append(i+1)
        
        return ans