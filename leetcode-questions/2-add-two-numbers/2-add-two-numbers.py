# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(dummy, l1, carry):
            while l1 or carry:
                if not l1 and carry:
                    dummy.next = ListNode(1)
                    return
                if carry:
                    dummy.next = ListNode((l1.val + 1) % 10)
                    carry = l1.val + 1 >= 10
                else:
                    dummy.next = ListNode(l1.val)
                l1 = l1.next
                dummy = dummy.next
                
        answer = dummy = ListNode(0)
        carry = False
        while l1 or l2 or carry:
            if l1 and l2:
                curr = l1.val + l2.val
                dummy.next = ListNode((curr+1) % 10) if carry else ListNode(curr % 10)    
                l1 = l1.next
                l2 = l2.next
                carry = curr + 1 >= 10 if carry else curr >= 10
                dummy = dummy.next
            elif l1:
                helper(dummy, l1, carry)
                return answer.next
            elif l2:
                helper(dummy, l2, carry)
                return answer.next
            else:
                dummy.next = ListNode(1)
                return answer.next
                
        return answer.next