# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root:    return 0
        count, covered = 0, set([None])
        
        def dfs(curr, parent):
            nonlocal count
            if not curr:    return
            
            dfs(curr.left, curr)
            dfs(curr.right, curr)
            
            if (parent == None and curr not in covered) or ((curr.left not in covered) or (curr.right not in covered)):
                count += 1
                covered.add(curr)
                covered.add(curr.left)
                covered.add(curr.right)
                covered.add(parent)
        
        dfs(root, None)
        
        return count