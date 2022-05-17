# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque()
        queue.append(root)
        res = deque()
        res.appendleft([root.val])
        
        while queue:
            levels = deque()
            while queue:
                curr = queue.popleft()
                if curr.left:   levels.append(curr.left)
                if curr.right:  levels.append(curr.right)
                
            queue = levels
            level = [node.val for node in levels]
            if level != []: res.appendleft(level)

        return res