class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(permutation, remaining):
            if len(permutation) == len(nums):
                res.append(list(permutation))
                return
            for i in range(len(remaining)):
                permutation.append(remaining[i])
                dfs(permutation, remaining[:i] + remaining[i+1:])
                permutation.pop()
        dfs([], nums)
        return res