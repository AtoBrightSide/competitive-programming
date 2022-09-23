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
        
        def buildTree(start):
            if not start:   return None
            if not start.next:  return TreeNode(start.val)
            
            mid = fast = start
            prev = None
            while fast and fast.next:
                prev = mid
                mid = mid.next
                fast = fast.next.next
            
            temp = mid.next
            prev.next = None
            
            node = TreeNode(mid.val)
            
            node.left = buildTree(start)
            node.right = buildTree(temp)
            
            return node
        
        return buildTree(head)