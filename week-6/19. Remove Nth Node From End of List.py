class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pt = ListNode(0)
        counter = head
        pt.next = head
        i,c=0,0
        while counter:
            counter = counter.next
            i+=1
        res=pt
        while pt:
            if c == i-n:
                pt.next = pt.next.next
                break
            pt = pt.next
            c+=1
        return res.next