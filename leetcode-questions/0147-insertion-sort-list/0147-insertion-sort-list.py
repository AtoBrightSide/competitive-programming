# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001, ListNode(head.val))
        head = head.next
        while head:
            curr = dummy
            while curr.next and head.val >= curr.next.val:
                curr = curr.next
            temp = curr.next
            curr.next = ListNode(head.val, temp)
            
            head = head.next
            
        return dummy.next