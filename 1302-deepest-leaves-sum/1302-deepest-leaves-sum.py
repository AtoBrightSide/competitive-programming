class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        summ = 0
        max_depth = 1
        nodes = []
        def dfs(node, curr_depth):
            if node is None:
                return
            if node.left is None and node.right is None:
                nodes.append((node.val, curr_depth))
                return
            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)
        dfs(root, 1)
        max_depth = max(*[i[1] for i in nodes])
        return sum([i[0] for i in nodes if i[1] == max_depth])
