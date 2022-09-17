# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:    return 0
        
        queue, depth = deque([root]), 0
        deepest = []
        while queue:
            levels = deque([])
            while queue:
                curr = queue.popleft()
                if curr.left:   levels.append(curr.left)
                if curr.right:  levels.append(curr.right)
            
            queue = levels
            deepest.append(list(levels.copy()))
            depth += 1
        
        return depth