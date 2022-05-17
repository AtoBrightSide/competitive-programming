# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        res = [[root.val]]
        flag = True
        while queue:
            levels = deque()
            while queue:
                curr = queue.popleft()
                if curr.left:
                    levels.append(curr.left)
                if curr.right:
                    levels.append(curr.right)
            
            queue = levels
            
            level = [node.val for node in levels]
            
            if flag: level.reverse()
            if level != []: res.append(level)
            
            flag = not flag
            
        return res