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
        self.used = {}
            
        return self.build(node.val)
    
    def build(self, root):
        root = Node(root)
        self.used[root.val] = root
        
        for neigh in self.graph[root.val]:
            if neigh not in self.used:   
                root.neighbors.append(self.build(neigh))
            else:
                root.neighbors.append(self.used[neigh])

        return root
        
    def traverse(self, node):
        if not node:    return
        
        for neighbor in node.neighbors:
            self.graph[node.val].append(neighbor.val)
            if neighbor.val not in self.graph:
                self.traverse(neighbor)
            