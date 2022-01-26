class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse l1 and l2
        dummy1 = l1
        num1,num2 = [],[]
        while dummy1:
            num1.append(str(dummy1.val))
            dummy1 = dummy1.next
        dummy2 = l2
        while dummy2:
            num2.append(str(dummy2.val))
            dummy2 = dummy2.next
        num1.reverse()
        num2.reverse()
        num1 = int("".join(num1))
        num2 = int("".join(num2))
        res = num1 + num2
        res = list(str(res))
        res.reverse()
        res = [int(num) for num in res]
        s = myres = ListNode(res[0])
        
        for num in res:
            myres.next = ListNode(num)
            myres = myres.next
        
        return s.next