# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = {}
        notRoot = set()
        
        for p, c, f in descriptions:
            new_p = graph.setdefault(p, TreeNode(p))
            new_c = graph.setdefault(c, TreeNode(c))
            
            if f:   new_p.left = new_c
            else:   new_p.right = new_c
            notRoot.add(c)
        
        for root in graph:
            if root not in notRoot: return graph[root]