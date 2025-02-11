# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = set()
        def traverse(node):
            if not node:    return 
            
            traverse(node.left)
            nodes.add(node.val)
            traverse(node.right)
        
        traverse(root)
        for node in nodes:
            if k - node in nodes and node != k - node:  return True
        
        return False