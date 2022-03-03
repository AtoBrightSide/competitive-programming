# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        myq = deque()
        myq.append(root)
        while myq:
            l = []
            for i in range(len(myq)):
                curr = myq.popleft()
                if curr.left:
                    myq.append(curr.left)
                    l.append(curr.left.val)
                else:
                    l.append(None)
                if curr.right:
                    myq.append(curr.right)
                    l.append(curr.right.val)
                else:
                    l.append(None)
            
            if l != l[::-1]:
                return False
            
        return True
