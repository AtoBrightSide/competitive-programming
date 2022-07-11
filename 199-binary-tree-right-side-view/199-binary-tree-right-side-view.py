# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:    return []
        right_side = [root.val]
        
        queue = deque([root])
        
        while queue:
            levels = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:   
                    queue.append(curr.left)
                    levels.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    levels.append(curr.right.val)
            
            if levels:  right_side.append(levels[-1])
            
        return right_side