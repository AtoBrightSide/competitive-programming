class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 0
        
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                nums[slow + 1] = nums[fast]
                slow += 1
            
            fast += 1
        
        return slow + 1
                