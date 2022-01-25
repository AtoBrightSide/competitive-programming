class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a linkedlist to store the merged list
        myList = ListNode(0)
        dummy = myList
        # iterate through one of the lists
        while list1 or list2:
            if list1 is None:
                dummy.next = list2
                list2 = list2.next
            elif list2 is None:
                dummy.next = list1
                list1 = list1.next
            else: 
                if list1.val <= list2.val:
                    dummy.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    dummy.next = ListNode(list2.val)
                    list2 = list2.next
            dummy = dummy.next
        return myList.next