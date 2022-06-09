class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        so_far = fast = slow = 0
        best = float('inf')
        
        while fast < len(nums):
            so_far += nums[fast]
            fast += 1
            
            while so_far >= target:
                best = min(best, fast - slow)
                so_far -= nums[slow]
                slow += 1
            
        return best if best != float("inf") else 0