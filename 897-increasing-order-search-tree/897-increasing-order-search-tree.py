# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        def inorder(root):
            if root == None:    return
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
            return
        inorder(root)
        
        nodes = ans = TreeNode(None)
        for node in res:
            ans.right = TreeNode(node)
            ans.left = None
            ans = ans.right
        
        return nodes.right