# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = []
        def dfs(node):
            if node.left:   dfs(node.left)
            nums.append(node.val)
            if node.right:  dfs(node.right)
        
        dfs(root)
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:    return False 
        return True