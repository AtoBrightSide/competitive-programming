class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(nums):
            l, r = 0, len(nums) - 1
            while l <= r:
                md = l + (r-l)//2
                
                if nums[md] == target:  return True
                if nums[md] > target:       r = md - 1
                elif nums[md] < target:     l = md + 1
        
        for row in matrix:
            if bs(row): return True
            
        return False