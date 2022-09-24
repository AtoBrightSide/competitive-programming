# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = defaultdict(list)
        nodes = set()
        for p, c, f in descriptions:
            graph[p].append([c, f])
            nodes.add(p)
        
        for p, c, f in descriptions:
            if c in nodes:  nodes.remove(c)
        
        
        def dfs(node):
            if node not in graph:   return TreeNode(node)
            
            root = TreeNode(node)
            for child, flag in graph[node]:
                if flag:    root.left = dfs(child)
                else:       root.right = dfs(child)
                
            
            return root
        
        for node in nodes:
            return dfs(node)
            