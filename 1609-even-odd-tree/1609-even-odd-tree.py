# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        levels = [[root.val]]
        while queue:
            curr_level = []
            for i in range(len(queue)):
                curr_node = queue[i]
                if curr_node.left:
                    curr_level.append(curr_node.left)
                if curr_node.right:
                    curr_level.append(curr_node.right)
            
            levels.append([node.val for node in curr_level])
            queue = curr_level
        
        for level, nodes in enumerate(levels):
            if not level % 2:
                prev = -1
                for node in nodes:
                    if node <= prev or node % 2 == 0:
                        return False
                    prev = node
            if level % 2:
                prev = float("inf")
                for node in nodes:
                    if node >= prev or node % 2:
                        return False
                    prev = node
        
        return True