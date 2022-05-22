# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []: return None
        res = []
        for l in lists:
            while l:
                heapq.heappush(res, l.val)
                l = l.next
        
        head = curr = ListNode(heapq.heappop(res)) if res else None
        
        while res:
            curr.next = ListNode(heapq.heappop(res))
            curr = curr.next
        
        
        return head