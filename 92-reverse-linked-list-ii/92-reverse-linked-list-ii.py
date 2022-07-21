# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        ans = head
        counter = 1
        while head:
            if counter == left:
                start = prev
                end = head
                while head and counter <= right:
                    temp_next = head.next
                    head.next = prev
                    prev = head
                    head = temp_next
                    counter += 1
                if start:   start.next = prev
                else:   ans = prev
                end.next = head
            prev = head
            if head:    head = head.next
            counter += 1
                
        return ans