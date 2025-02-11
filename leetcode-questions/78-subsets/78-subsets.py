class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        for i in range(pow(2, n)):
            subsets = set()
            for j in range(n):
                if i & (1 << j) != 0:
                    subsets.add(nums[j])
            res.append(list(subsets))
        
        return res