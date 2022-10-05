# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        levels_counter = 0
        while queue:
            levels_counter += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            start, end = 0, len(queue) - 1
            if levels_counter % 2 != 0:
                while start <= end:
                        queue[start].val, queue[end].val = queue[end].val, queue[start].val
                        start += 1
                        end -= 1

        return root
