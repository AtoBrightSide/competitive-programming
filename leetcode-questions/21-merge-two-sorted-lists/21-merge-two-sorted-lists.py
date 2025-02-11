# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def mergeLists(node1, node2):
            if not node1 or not node2:  return node1 if node1 else node2
            
            if node1.val < node2.val:
                node1.next = mergeLists(node1.next, node2)
                return node1
            else:
                node2.next = mergeLists(node1, node2.next)
                return node2
        
        return mergeLists(list1, list2)