# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root]) 
        
        while queue: 
            size = len(queue)  
            level = deque()

            for i in range(size): 
                curr = queue.popleft() 
                if curr: 
                    level.append(curr.left) 
                    level.append(curr.right) 
            queue = level
            listval = []
            for i in level:
                if i:
                    listval.append(i.val)
                else:
                    listval.append(i)
            left = 0 
            right = len(listval) - 1

            while left <= right:
                if listval[left] != listval[right]:
                    return False
                left +=1
                right -=1

        return True