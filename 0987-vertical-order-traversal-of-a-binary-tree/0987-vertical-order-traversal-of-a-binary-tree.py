# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = defaultdict(list)
        cols = set()
        def traverse(node, row, col):
            if node:
                cols.add(col)
                order[(row, col)].append(node.val)
                traverse(node.left, row + 1, col - 1)
                traverse(node.right, row + 1, col + 1)
        
        traverse(root, 0, 0)
        ans = [[] for _ in range(len(cols))] 
        min_col = abs(min(cols))
        items = sorted(order.items(), key=lambda x:(x[0][1], x[0][0]))
        for key, val in items:
            val.sort()
            ans[key[1] + min_col].extend(val)
        
        return ans
            
            