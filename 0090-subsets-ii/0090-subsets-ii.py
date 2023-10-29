class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        
        def backtrack(i, so_far):
            if i == len(nums) + 1:
                return 
            
            subsets.add(tuple(sorted(so_far)))
            for j in range(i, len(nums)):
                so_far.append(nums[j])
                backtrack(j + 1, so_far)
                so_far.pop()
            
        backtrack(0, [])
        return list(subsets)