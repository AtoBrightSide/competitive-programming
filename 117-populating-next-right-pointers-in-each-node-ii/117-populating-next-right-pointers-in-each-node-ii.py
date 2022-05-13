"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        myqueue = deque()
        if root is not None:
            myqueue.append(root)
        
        while myqueue:
            level = deque()
            while myqueue:
                curr = myqueue.popleft()
                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
                
            myqueue = level
        
        return root