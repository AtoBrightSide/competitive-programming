# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root)
                inorder(root.right)
            return
        
        inorder(root)
        
        the_copy = copy.deepcopy(res)
        the_copy.sort(key=lambda x:x.val)
        
        for i in range(len(res)):
            print(res[i].val, the_copy[i].val)
            if res[i].val != the_copy[i].val:
                res[i].val = the_copy[i].val
        