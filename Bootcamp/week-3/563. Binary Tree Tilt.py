# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(root):
            nonlocal total 
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            total += abs(l-r)
            return l+r+root.val
        dfs(root)
        return total
