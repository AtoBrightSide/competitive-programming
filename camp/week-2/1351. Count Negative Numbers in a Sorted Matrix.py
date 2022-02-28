class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for col in grid:
            for elt in col:
                count += 1 if elt<0 else 0
                
        return count
