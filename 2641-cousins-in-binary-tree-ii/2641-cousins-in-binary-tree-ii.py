# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        levels = [[root]]
        sibling = {}
        while queue:
            curr_level = []
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                
                if curr_node.left and curr_node.right:
                    sibling[curr_node.left] = curr_node.right.val
                    sibling[curr_node.right] = curr_node.left.val
                
                if curr_node.left:
                    curr_level.append(curr_node.left)
                    queue.append(curr_node.left)
                if curr_node.right:
                    curr_level.append(curr_node.right)
                    queue.append(curr_node.right)
                
            if curr_level:  levels.append(curr_level)
        
        new_values = {root: 0}
        for level in levels:
            total = sum([n.val for n in level])
            for node in level:
                new_values[node] = total - node.val - (sibling[node] if node in sibling else 0)
        
        for key, value in new_values.items():   key.val = value
        
        return root