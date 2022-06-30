class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        
        while nums[0] != nums[-1]:
            curr = nums.pop()
            count += (curr - nums[0])
            nums[0] = curr
            nums[-1] += count
            
        return count