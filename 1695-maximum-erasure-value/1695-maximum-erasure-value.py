class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = best = curr = 0
        window = set()
        
        '''
                ,
        4 2 4 5 6
          ,
        window=2 4 5
        curr=11
        best=11
        '''
        
        for i, num in enumerate(nums):
            while num in window:
                window.remove(nums[left])
                curr -= nums[left]
                left += 1
            window.add(num)
            curr += num
            best = max(best, curr)
            
        return best