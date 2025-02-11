class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        
        def recursive(i, so_far):
            if i == len(nums) + 1:
                return
            
            subsets.append(so_far.copy())
            for j in range(i, len(nums)):
                so_far.append(nums[j])
                recursive(j + 1, so_far)
                so_far.pop()
        
        recursive(0, [])
        
        return subsets