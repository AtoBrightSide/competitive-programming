# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node, depth):
            if not node:
                return [node, depth]
            
            left = traverse(node.left, depth + 1)
            right = traverse(node.right, depth + 1)
            
            if left[1] == right[1]:
                return [node, left[1] + 1]
            if left[1] > right[1]:
                return [left[0], left[1] + 1]
            else:
                return [right[0], right[1] + 1]
            
        return traverse(root, 0)[0]
            