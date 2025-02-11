"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':        
        myqueue = deque()
        if root is not None:
            myqueue.append(root)
        
        while myqueue:
            temp = deque()
            while myqueue:
                curr = myqueue.popleft()
                if curr.left:
                    temp.append(curr.left)
                    temp.append(curr.right)
                
            for i in range(len(temp) - 1):
                temp[i].next = temp[i+1]
            
            myqueue = temp
        return root