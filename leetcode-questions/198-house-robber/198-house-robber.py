class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = [nums[0]]
        res.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            res.append(max(nums[i]+res[i-2], res[i-1]))
                
        return (res[-1])
                    