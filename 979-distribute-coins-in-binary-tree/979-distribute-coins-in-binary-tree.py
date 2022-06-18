# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if node is None:    return 0
            
            LEFT = dfs(node.left)
            
            RIGHT = dfs(node.right)
            
            ans += abs(LEFT) + abs(RIGHT)
            
            return node.val + RIGHT + LEFT - 1
        
        dfs(root)
        
        return ans