# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        ans = head
        while head:
            nodes.append(head)
            head = head.next
        
        ptr, i = len(nodes)-1, float("inf")
        for i in range(len(nodes)//2):
            nodes[i].next = nodes[ptr] 
            nodes[ptr].next = nodes[i+1]
            ptr -= 1
        
        if i < len(nodes) - 1:   nodes[i+1].next = None