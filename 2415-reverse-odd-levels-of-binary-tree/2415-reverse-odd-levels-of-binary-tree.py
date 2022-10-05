# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(level, left, right):
            if left or right:
                if level % 2:
                    left.val, right.val = right.val, left.val

                dfs(level + 1, left.left, right.right)
                dfs(level + 1, left.right, right.left)
        
        dfs(1, root.left, root.right)
        return root