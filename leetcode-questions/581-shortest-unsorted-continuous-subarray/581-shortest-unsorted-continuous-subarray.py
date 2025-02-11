class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        pt = False
        first = last = best = 0
        copied = nums.copy()
        nums.sort()
        
        while last<len(nums):    
            if copied[last] != nums[last]:
                pt = True
                best = max(best, last-first+1)
            elif not pt:
                first += 1
            last += 1
                
        return best
