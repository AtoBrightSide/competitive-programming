# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        return self.dfs(root, 0, targetSum)
        
    def dfs(self, root, val, target):
        
        if (not root.left and not root.right) and val+root.val == target:
            return True
        
        l,r = False, False
        if root.left:
            l = self.dfs(root.left, val + root.val, target)
        
        if root.right:
            r = self.dfs(root.right, val + root.val, target)
        
        return l or r
