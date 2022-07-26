# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def dfs(node):
            nonlocal ans
            if not node: return False
            
            mid = True if node == p or node == q else False
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if (mid and left) or (mid and right) or (left and right):
                ans = node
            
            return mid or left or right
        dfs(root)
        return ans