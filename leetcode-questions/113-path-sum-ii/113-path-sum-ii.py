# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        if not root:    return paths
        
        def dfs(node, so_far, path):
            nonlocal paths
            if not node.left and not node.right:
                if so_far + node.val == targetSum:
                    path.append(node.val)
                    paths.append(path.copy())
                    if path:    path.pop()
                return
            
            path.append(node.val)
            if node.left:   dfs(node.left, so_far + node.val, path)
            if node.right:  dfs(node.right, so_far + node.val, path)
            if path:    path.pop()
            
        
        dfs(root, 0, [])
        return paths