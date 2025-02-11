class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        minMoves = 0
        nums.sort()
        curr = len(nums) // 2
        
        for num in nums:
            minMoves += abs(nums[curr] - num)
        
        return minMoves