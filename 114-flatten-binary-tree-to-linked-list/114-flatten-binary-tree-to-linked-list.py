# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        def dfs(node):
            if not node:    return
            
            nodes.append(node)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        for i in range(1, len(nodes)):
            root.left = None
            root.right = nodes[i]
            root = root.right