# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:    return TreeNode(val)
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            
            if curr.val > val:
                if curr.left:   queue.append(curr.left)
                else:   curr.left = TreeNode(val)
            else:
                if curr.right:  queue.append(curr.right)
                else:   curr.right = TreeNode(val)
        
        return root