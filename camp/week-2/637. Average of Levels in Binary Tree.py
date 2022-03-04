# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        myq = deque()
        res = [root.val]
        myq.append(root)
        while myq:
            lst = []
            for i in range(len(myq)):
                curr = myq.popleft()
                if curr.left:
                    myq.append(curr.left)
                    lst.append(curr.left.val)
                if curr.right:
                    myq.append(curr.right)
                    lst.append(curr.right.val)
            if lst == []:
                break
            res.append(sum(lst)/len(lst))
        return res
