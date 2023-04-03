# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            nodes = [root.val]
            queue = deque([root])

            while queue:
                level = []
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    if curr.left:
                        level.append(curr.left.val)
                        queue.append(curr.left)
                    if curr.right:
                        level.append(curr.right.val)
                        queue.append(curr.right)

                if level:
                    nodes.append(level[-1])

            return nodes
        return []