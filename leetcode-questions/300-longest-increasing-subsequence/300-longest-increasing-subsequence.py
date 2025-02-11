class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        sequence = [float('inf')] * len(nums)
        sequence[0] = nums[0]
        
        def binarySearch(num):
            l, r = 0, len(nums) - 1
            
            while l <= r:
                md = l + (r - l)//2
                if sequence[md] >= num:
                    r = md - 1
                else:
                    l = md + 1
            return l
        
        
        for i in range(1, len(nums)):
            pos = binarySearch(nums[i])
            sequence[pos] = nums[i]
            
        
        return len(sequence) - sequence.count(float('inf'))
        