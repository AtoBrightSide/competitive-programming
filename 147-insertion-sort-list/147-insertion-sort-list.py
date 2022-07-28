# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = ListNode(-5001)
        
        while head:
            temp = sorted_list
            while temp.next and not temp.val <= head.val <= temp.next.val:
                temp = temp.next
            
            curr = temp.next
            curr2 = head.next
            temp.next = head
            head.next = curr
            head = curr2
            
        return sorted_list.next