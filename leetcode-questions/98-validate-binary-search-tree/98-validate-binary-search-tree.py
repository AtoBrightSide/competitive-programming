# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, higher):
            if not node:    return True
            
            if not (lower < node.val < higher): return False
            
            l = r = True
            if node.left:   l = dfs(node.left, lower, node.val)
            if node.right:  r = dfs(node.right, node.val, higher)
            
            return l and r
        
        return dfs(root, -float("inf"), float("inf"))