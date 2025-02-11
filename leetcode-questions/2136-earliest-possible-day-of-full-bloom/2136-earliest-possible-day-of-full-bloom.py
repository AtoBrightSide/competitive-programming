class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plantGrowPair = sorted([[plantTime[i], growTime[i]] for i in range(len(growTime))], key=lambda x:-x[1])
                
        length = 0
        start = 0
        
        for pt, gt in plantGrowPair:
            start += pt
            length = max(length, start + gt)
        
        return length