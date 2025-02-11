# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:   return head
        
        prev = None
        res = ans = ListNode()
        curr = head
        
        while curr:
            while curr and ((prev and prev.val == curr.val) or (curr.next and curr.val == curr.next.val)):
                prev = curr
                curr = curr.next

            ans.next = curr
            ans = ans.next
            prev = curr
            if curr:   curr = curr.next
            
        return res.next