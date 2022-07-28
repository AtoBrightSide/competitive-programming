# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = dummy = ListNode(0)
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
            
        nodes.sort()
        for node in nodes:
            dummy.next = ListNode(node)
            dummy = dummy.next
            
        return answer.next