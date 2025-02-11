class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        right, res = 1, [intervals[0]]
        
        while right < len(intervals):
            if intervals[right][0] > res[-1][1]:
                res.append(intervals[right])
                right += 1
            else:
                while right < len(intervals) and (res[-1][1] >= intervals[right][1] or res[-1][1] >= intervals[right][0]):
                    res[-1][1] = max(res[-1][1], intervals[right][1])
                    right += 1
                
        return res
    '''
    
    (0,2) (0,2) (1,3) (2,3) (3,3) (4,5) (4,6) (5,5)
    
    '''