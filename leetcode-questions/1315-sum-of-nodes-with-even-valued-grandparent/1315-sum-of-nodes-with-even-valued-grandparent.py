# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return []
        total = 0
        def dfs(node, p, gp):
            nonlocal total
            if not node:    return
            
            if gp:  total += node.val if gp.val % 2 == 0 else 0
            
            if node.left:   dfs(node.left, node, p)    
            if node.right:  dfs(node.right, node, p)
        
        dfs(root, None, None)
        
        return total