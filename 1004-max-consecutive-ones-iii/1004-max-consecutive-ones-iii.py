class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow = fast = best = 0
        count = (1 if nums[fast] == 0 else 0)
        while slow < len(nums) and fast < len(nums):
            while fast < len(nums) and count <= k:
                best = max(best, fast - slow + 1)
                fast += 1
                if fast < len(nums) and nums[fast] == 0:
                    count += 1
            count -= (1 if nums[slow] == 0 else 0)
            slow += 1
            
        return best