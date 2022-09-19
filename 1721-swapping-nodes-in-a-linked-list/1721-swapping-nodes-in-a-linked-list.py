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
        answer = swapped = ListNode(0)
        while head:
            while head in swap:
                if head == swap[0]:
                    swapped.next = ListNode(swap[-1].val)
                else:
                    swapped.next = ListNode(swap[0].val)
                swapped = swapped.next
                head = head.next
            swapped.next = head
            swapped = swapped.next
            if head:   head = head.next
        
        return answer.next 