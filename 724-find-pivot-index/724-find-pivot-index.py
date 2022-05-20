class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [num for num in nums]
        rightSum = [num for num in nums]
        L = len(nums)
        for i in range(1, L):
            leftSum[i] += leftSum[i-1]
            rightSum[-i - 1] += rightSum[-i]
            
        for j in range(len(leftSum)):
            if leftSum[j] == rightSum[j]: return j
            
        return -1