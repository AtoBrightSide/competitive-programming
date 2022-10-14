# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def traverse(node, left):
            nonlocal ans
            if not node:    return left
            
            curr = 1 + traverse(node.left, left)
            if curr == k:   ans = node.val
            return traverse(node.right, curr)
        
        traverse(root, 0)
        return ans