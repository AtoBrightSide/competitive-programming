class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        
        moves = 0
        sub = 0
        
        for i in range(len(nums)):
            nums[i] -= sub
            if nums[i] != 0:
                moves += 1
                sub += nums[i]
        
        return moves
                