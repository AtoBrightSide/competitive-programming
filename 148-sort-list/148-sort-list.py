# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1, list2):
            ans = dummy = ListNode(0)
            while list1 or list2:
                if list1 and list2:
                    if list1.val <= list2.val:
                        dummy.next = list1
                        list1 = list1.next
                    else:
                        dummy.next = list2
                        list2 = list2.next
                    dummy = dummy.next
                elif list1:
                    dummy.next = list1
                    list1 = list1.next
                    dummy = dummy.next
                elif list2:
                    dummy.next = list2
                    list2 = list2.next
                    dummy = dummy.next
            return ans.next
        
        def getMid(list1):
            fast = list1
            while fast and fast.next:
                fast = fast.next.next
                list1 = list1.next if fast and fast.next else list1
            
            return list1
        
        def recur(head):
            if not head or not head.next:    return head
            
            mid = getMid(head)
            temp = mid.next
            mid.next = None
            
            left = recur(head)
            right = recur(temp)
            
            return merge(left, right)
        
        return recur(head)