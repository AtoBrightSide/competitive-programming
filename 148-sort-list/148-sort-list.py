# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        
        nodes.sort()
        ans = dummy = ListNode(0)
        for n in nodes:
            dummy.next = ListNode(n)
            dummy = dummy.next
        
        return ans.next