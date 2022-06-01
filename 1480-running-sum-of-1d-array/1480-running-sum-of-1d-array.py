class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = [num for num in nums]
        
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]
            
        return prefixSum