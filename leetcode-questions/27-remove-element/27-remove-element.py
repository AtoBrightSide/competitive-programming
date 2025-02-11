class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        for num in nums:
            if num != val:
                nums[curr] = num
                curr += 1
                
        return curr