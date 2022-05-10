class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for c in range(k, len(nums)):
                        if (nums[i] + nums[j] + nums[k]) == nums[c]:
                            count += 1
                        
                        
        return count