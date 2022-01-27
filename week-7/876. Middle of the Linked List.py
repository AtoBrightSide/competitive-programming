# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        i,c=0,0
        while temp:
            temp = temp.next
            c+=1
        while head:
            if i == c//2:
                return head
            i+=1
            head = head.next