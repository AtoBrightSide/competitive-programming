# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    return []
        
        levels = [[root.val]]
        queue = deque([root])
        
        while queue:
            curr_level = deque()
            temp = []
            while queue:
                node = queue.popleft()
                if node.left:
                    curr_level.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    curr_level.append(node.right)
                    temp.append(node.right.val)
            
            if temp:    levels.append(temp)
            queue = curr_level
            
        return levels