# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def findAncestor(node):
            nonlocal ans
            if not node:
                return
            if q.val <= node.val <= p.val or q.val >= node.val >= p.val:
                ans = node
                return
            
            if node.val > q.val:
                findAncestor(node.left)
            
            if node.val < q.val:
                findAncestor(node.right)
        
        findAncestor(root)
        return ans