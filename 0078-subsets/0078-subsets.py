class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = set()
        def backtrack(i, so_far):
            
            all_subsets.add(tuple(so_far))
            for j in range(i + 1, len(nums)):
                backtrack(j, so_far + [nums[j]])
        
        for i, num in enumerate(nums):
            backtrack(i, [num])
        
        return [[]] + [list(subset) for subset in all_subsets]