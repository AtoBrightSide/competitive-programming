class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = [rec1[0], rec1[2]]
        y1 = [rec1[1], rec1[3]]
        x2 = [rec2[0], rec2[2]]
        y2 = [rec2[1], rec2[3]]
        
        if x1[0] == x1[1] or x2[0] == x2[1] or y1[0] == y1[1] or y2[0] == y2[1]:
            return False
        if (x2[0] <= x1[0] < x2[1]) or (x1[0] <= x2[0] < x1[1]):
            if y2[0] <= y1[0] <= y2[1] or y1[0] <= y2[0] <= y1[1]:
                return True
            
            
        return False