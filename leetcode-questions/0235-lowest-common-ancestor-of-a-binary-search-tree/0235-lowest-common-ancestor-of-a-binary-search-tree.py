# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def findAncestor(node = 2):
            
            if (p.val >= node.val and q.val <= node.val) or (q.val >= node.val and p.val <= node.val):
                return node
            
            if p.val < node.val:
                return findAncestor(node.left)
            if p.val > node.val:
                return findAncestor(node.right)
        
        
        return findAncestor(root)
            