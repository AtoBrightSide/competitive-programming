# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = None
        
        def traverse(node):
            nonlocal ancestor
            if not node:
                return False
            
            curr = node == p or node == q
            
            left = traverse(node.left)
            right = traverse(node.right)
            
            if (left and curr) or (right and curr) or (left and right):
                ancestor = node
            
            return left or right or curr
        
        traverse(root)
        return ancestor
            
            
            