# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def buildTree(l, r):
            if l >= r: 
                return TreeNode(nums[r]) if l == r else None
            
            md = l + (r - l)//2
            node = TreeNode(nums[md])
            node.left = buildTree(l, md - 1)
            node.right = buildTree(md + 1, r)
            
            return node
        
        return buildTree(0, len(nums)-1)