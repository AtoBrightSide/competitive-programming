# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:    return None
        def traverse(node):
            if not node.left:    return node
            if node.left:   return traverse(node.left)
            
        if root.val == key:
            if not root.left and not root.right:    return None
            if root.right:
                last = traverse(root.right)
                last.left = root.left
                return root.right
            return root.left
        
        def delete(node, parent, left):
            if not node:    return
            
            if not node.left and not node.right:
                if not parent:  return None
                if left:    parent.left = None
                else:       parent.right = None
            elif node.right:
                last = traverse(node.right)
                last.left = node.left
                if parent:
                    if left:        parent.left = node.right
                    else:           parent.right = node.right
            else:
                if parent:
                    if left:    parent.left = node.left
                    else:       parent.right = node.left
            
        def doIt(node, par, flag):
            if node:
                if node.val == key: return delete(node, par, flag)
                if node.val > key:  return doIt(node.left, node, True)
                if node.val < key:  return doIt(node.right, node, False)
        
        doIt(root, None, None)
        return root