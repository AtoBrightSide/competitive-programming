# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for i in range(len(lists)):
            while lists[i]:
                res.append(lists[i].val)
                lists[i] = lists[i].next
        
        heapq.heapify(res)
        if res==[] or len(lists)==0:
            return None
        head = ans = ListNode(heapq.heappop(res))
        for i in range(len(res)):
            ans.next = ListNode(heapq.heappop(res))
            ans = ans.next
        return head
