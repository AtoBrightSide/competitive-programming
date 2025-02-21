# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = set([0])

        def traverse(root):
            if root.left:
                root.left.val = 2 * root.val + 1
                self.nodes.add(root.left.val)
                traverse(root.left)
            if root.right:
                root.right.val = 2 * root.val + 2
                self.nodes.add(root.right.val)
                traverse(root.right)

        root.val = 0
        traverse(root)

    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
