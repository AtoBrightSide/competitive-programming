# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def traverse(node, curr):
            nonlocal count
            if not node:    return
            
            if node.val >= curr:
                count += 1
            
            traverse(node.left, max(node.val, curr))
            traverse(node.right, max(node.val, curr))
        
        traverse(root, root.val)
        return count
                