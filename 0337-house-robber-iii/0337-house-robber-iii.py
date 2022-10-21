# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        remember = {}
        def traverse(node, robbed):
            if not node:    
                return 0
            if (node, robbed) in remember:
                return remember[(node, robbed)]
            
            pick = dontPick = 0
            if robbed:
                dontPick = traverse(node.left, False) + traverse(node.right, False)
            else:
                pick = max(node.val + traverse(node.left, True) + traverse(node.right, True), traverse(node.left, False) + traverse(node.right, False))
            
            remember[(node, robbed)] = max(pick, dontPick)
            return remember[(node, robbed)]
            
        return max(traverse(root, True), traverse(root, False))
    