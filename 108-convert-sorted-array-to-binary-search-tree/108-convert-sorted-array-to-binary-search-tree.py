# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(l, r):
            if l > r:   return None
            
            md = l + ((r - l) // 2)
            node = TreeNode(nums[md])
            node.left = buildBST(l, md - 1)
            node.right = buildBST(md + 1, r)
                
            return node
        
        return buildBST(0, len(nums)-1)