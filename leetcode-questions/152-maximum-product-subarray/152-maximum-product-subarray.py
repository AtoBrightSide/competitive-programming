class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prefix, suffix = [nums[0]], [nums[-1]]
        L = len(nums) - 1
        for i in range(1, len(nums)):
            if prefix[-1] != 0: 
                prefix.append(prefix[-1] * nums[i])
            else:
                prefix.append(nums[i])
            if suffix[-1] != 0:
                suffix.append(suffix[-1] * nums[L - i])
            else:
                suffix.append(nums[L-i])

        return max(max(prefix + suffix), max(nums))