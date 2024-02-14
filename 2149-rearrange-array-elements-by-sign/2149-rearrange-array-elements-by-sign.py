class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums:
            if num > 0: pos.append(num)
            if num < 0: neg.append(num)
        i = 0
        modified = []
        while i < len(neg):
            if i < len(pos):    
                modified.append(pos[i])
            
            if i < len(neg):    
                modified.append(neg[i])
            
            i += 1
        
        return modified