# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = smaller_p = ListNode(0)
        bigger = bigger_p = ListNode(0)
        
        while head:
            if head.val < x:
                smaller_p.next = ListNode(head.val)
                smaller_p = smaller_p.next
            elif head.val >= x:
                bigger_p.next = ListNode(head.val)
                bigger_p = bigger_p.next
            
            head = head.next
            
        bigger = bigger.next
        while bigger:
            smaller_p.next = bigger
            bigger = bigger.next
            smaller_p = smaller_p.next
            
        return smaller.next