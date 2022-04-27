class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        slow = fast = best = 0
        total = nums[0]
        while slow < len(nums):
            while fast<len(nums) and nums[fast]*(fast-slow+1) <= total+k:
                best = max(best, fast-slow+1)
                fast += 1
                total += nums[fast] if fast<len(nums) else 0
            total -= nums[slow]
            slow += 1
        return best
