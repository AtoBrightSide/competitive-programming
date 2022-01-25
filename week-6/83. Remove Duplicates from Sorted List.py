class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        while dummy:
            if dummy.next and dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
                continue
            dummy = dummy.next
        return head