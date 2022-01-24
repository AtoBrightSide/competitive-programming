# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        # temp=1
        temp = ListNode(head.val)
        # head=2
        head = head.next
        while head:
            # rev=2
            rev = ListNode(head.val)
            rev.next = temp
            head = head.next
            temp = rev
            
        return temp