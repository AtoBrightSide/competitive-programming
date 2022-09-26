"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        nodes = []
        def dfs(node):
            nonlocal nodes
            if not node:    return
            
            nodes.append(node.val)
            for child in node.children:
                dfs(child)
        
        dfs(root)
        return nodes