# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recur(pre, ino):
            if not pre or not ino: return None
            
            root = TreeNode(pre[0])
            md = ino.index(root.val)
            root.left = recur(pre[1:md+1], ino[:md])
            root.right = recur(pre[md+1:], ino[md+1:])
            
            return root
        
        return recur(preorder, inorder)