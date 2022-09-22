# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recur(node):
            if not node:    return None
        
            start = node.next
            if start:
                temp = start.next
                start.next = node
                node.next = recur(temp)
            
            return start if start else node
        
        return recur(head)