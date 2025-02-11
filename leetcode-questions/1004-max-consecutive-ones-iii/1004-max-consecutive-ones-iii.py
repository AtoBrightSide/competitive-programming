class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow = fast = 0
        longest = 0
        
        while fast < len(nums):
            while fast < len(nums) and (k > 0 or nums[fast] != 0):
                k -= (1 if nums[fast] == 0 else 0)
                fast += 1
            
            longest = max(longest, fast - slow)
            k += 1 if slow < len(nums) and nums[slow] == 0 else 0
            slow += 1
        
        return longest