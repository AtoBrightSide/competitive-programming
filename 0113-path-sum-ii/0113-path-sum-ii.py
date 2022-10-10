# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        paths = []
        def dfs(node, path, so_far):
            if not node.left and not node.right:
                if so_far == targetSum:
                    paths.append(path.copy())
                return
            
            if node.left:
                path.append(node.left.val)
                dfs(node.left, path, so_far + node.left.val)
                path.pop()
            
            if node.right:
                path.append(node.right.val)
                dfs(node.right, path, so_far + node.right.val)
                path.pop()
        
        if root:    dfs(root, [root.val], root.val)
        return paths