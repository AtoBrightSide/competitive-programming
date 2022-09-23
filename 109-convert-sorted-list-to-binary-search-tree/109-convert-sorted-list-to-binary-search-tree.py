# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        
        def buildTree(start, end):
            if start == end:    return None
            
            mid = fast = start
            while fast != end and fast.next != end:
                mid = mid.next
                fast = fast.next.next
            
            node = TreeNode(mid.val)
            node.left = buildTree(start, mid)
            node.right = buildTree(mid.next, end)
            
            return node
            
        return buildTree(head, None)