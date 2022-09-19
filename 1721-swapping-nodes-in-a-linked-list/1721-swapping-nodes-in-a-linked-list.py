# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        swap = []
        def reverseList(node):
            i, prev = 1, None
            while node:
                if i == k:  swap.append(node)
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                i += 1
            
            return prev
        
        head = reverseList(reverseList(head))
        
        swap[0].val, swap[1].val = swap[1].val, swap[0].val
        return head