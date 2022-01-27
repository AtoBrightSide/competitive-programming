# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        dummy = head
        while dummy:
            nums.append(dummy.val)
            dummy = dummy.next
        nums.reverse()
        for num in nums:
            if num != head.val:
                return False
            head = head.next
        return True