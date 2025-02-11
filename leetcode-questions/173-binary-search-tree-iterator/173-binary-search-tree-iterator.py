# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.arr = []
        
        def inorder(root):
            if root:
                inorder(root.left)
                self.arr.append(root.val)
                inorder(root.right)
        
        inorder(self.root)
        self.arr.sort(reverse=True)
        
    def next(self) -> int:
        return self.arr.pop()

    def hasNext(self) -> bool:
        return True if self.arr != [] else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()