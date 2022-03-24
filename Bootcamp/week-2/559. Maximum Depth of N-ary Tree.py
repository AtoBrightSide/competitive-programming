"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        return self.dfs(root, 1)    
    
    def dfs(self, root, c):
        # print(root.val, c)
        maxdepth = c
        if root.children:
            for i in range(len(root.children)):
                maxdepth = max(maxdepth, self.dfs(root.children[i], c+1))
        
        return maxdepth
