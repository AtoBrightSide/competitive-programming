# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque()
        queue.append(original)
        queue2 = deque()
        queue2.append(cloned)
        
        while queue:
            curr = queue.popleft()
            curr2 = queue2.popleft()
            if curr == target:
                return curr2
            if curr.left: 
                queue.append(curr.left)
                queue2.append(curr2.left)
                
            if curr.right: 
                queue.append(curr.right)
                queue2.append(curr2.right)
