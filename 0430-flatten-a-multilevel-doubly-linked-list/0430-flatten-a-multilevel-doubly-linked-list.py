"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def flattenChild(node):
            ans = node
            prev = None 
            while node:
                if node.child:
                    start, end = flattenChild(node.child)
                    
                    node.child = None
                    temp = node.next
                    
                    node.next = start
                    start.prev = node
                    
                    if end:
                        end.next = temp
                    if temp:
                        temp.prev = end
                    
                    node = temp
                    prev = end
                else:
                    prev = node
                    node = node.next

            return ans, prev
        
        ans = head
        flattenChild(head)
        return ans