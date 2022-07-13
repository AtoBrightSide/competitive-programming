# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    return []
        
        queue = deque([root])
        res = [[root.val]]
        while queue:
            levels = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    levels.append(curr.left.val)
                    queue.append(curr.left)
                if curr.right:
                    levels.append(curr.right.val)
                    queue.append(curr.right)
            
            if levels:  res.append(levels)
            
        return res