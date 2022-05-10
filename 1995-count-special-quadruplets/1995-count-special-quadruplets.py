class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        possibleSums = defaultdict(int)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i-1, -1, -1):
                for k in range(j-1, -1, -1):
                    curr = nums[i] + nums[j] + nums[k]
                    if curr in possibleSums:
                            count += possibleSums[curr]
            possibleSums[nums[i]] += 1
                        
        return count