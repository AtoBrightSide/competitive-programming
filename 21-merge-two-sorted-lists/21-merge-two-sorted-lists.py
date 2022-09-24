# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = dummy = ListNode()
        
        def mergeLists(node1, node2):
            nonlocal dummy
            if not node1 and not node2:  return
            
            if node1 and node2:
                if node1.val < node2.val:
                    dummy.next = node1
                    dummy = dummy.next
                    mergeLists(node1.next, node2)
                else:
                    dummy.next = node2
                    dummy = dummy.next
                    mergeLists(node1, node2.next)
            elif node1:
                dummy.next = node1
                dummy = dummy.next
                mergeLists(node1.next, node2)
            elif node2:
                dummy.next = node2
                dummy = dummy.next
                mergeLists(node1, node2.next)
        
        mergeLists(list1, list2)
        return merged.next