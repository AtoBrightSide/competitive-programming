# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        def calculateSum(node):
            if not node:	return 0

            return node.val + calculateSum(node.left) + calculateSum(node.right)


        sum_so_far = calculateSum(root)
        def inOrderTraversal(current_node):
            nonlocal sum_so_far
            if not current_node:	return 0
            if not current_node.left and not current_node.right:
                temp = current_node.val
                current_node.val = sum_so_far
                # print(current_node, temp)
                return temp
            p = inOrderTraversal(current_node.left)
            sum_so_far -= p
            # if current_node.val == 4:   print(sum_so_far, p)
            temp = current_node.val
            current_node.val = sum_so_far
            sum_so_far -= temp
            
            
            return inOrderTraversal(current_node.right)
        
        inOrderTraversal(root)

        return root 