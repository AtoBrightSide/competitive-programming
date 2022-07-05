class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:  return 0
        nums.sort()
        ans = count = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:    count += 1
            elif nums[i] == nums[i+1]:  continue
            else:
                ans = max(ans, count)
                count = 1
                
        return max(ans, count)