"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        self.graph = defaultdict(list)
        self.traverse(node)
        used = {}
        def build(root):
            if not root:
                return None
            
            root = Node(root)
            used[root.val] = root
            for neigh in self.graph[root.val]:
                if neigh not in used:   
                    root.neighbors.append(build(neigh))
                else:
                    root.neighbors.append(used[neigh])
            
            return root
            
        return build(node.val)
        
    def traverse(self, node):
        if not node:    return
        
        for neighbor in node.neighbors:
            self.graph[node.val].append(neighbor.val)
            if neighbor.val not in self.graph:
                self.traverse(neighbor)
            