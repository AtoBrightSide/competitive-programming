# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        
        N = len(nodes)
        maxSum = 0
        for i in range(int(len(nodes)/2)):
            maxSum = max(maxSum, nodes[i] + nodes[N-1-i])
            
        return maxSum