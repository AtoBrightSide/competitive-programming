class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                temp=(nums[i]-nums[i+1])+1
                nums[i+1]= nums[i+1]+(nums[i]-nums[i+1])+1
                count= count + temp
        return count
