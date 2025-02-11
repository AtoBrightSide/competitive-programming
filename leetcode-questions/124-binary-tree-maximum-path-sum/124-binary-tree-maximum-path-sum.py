# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxPath = -float("inf")
        def traverse(node):
            nonlocal maxPath
            if not node:        return 0
            
            left = max(0, traverse(node.left))
            right = max(traverse(node.right), 0)
            
            maxPath = max(maxPath, left + right + node.val, node.val)
            
            return max(left + node.val, right + node.val)
        
        traverse(root)
        return maxPath