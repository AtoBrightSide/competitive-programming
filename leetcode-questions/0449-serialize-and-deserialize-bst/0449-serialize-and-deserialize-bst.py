# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:    return ""
        queue = deque([root])
        ans = [str(root.val)]
        
        while queue:
            curr = queue.popleft()
            if curr.left:
                ans.append(str(curr.left.val))
                queue.append(curr.left)
            else:
                ans.append("X")
            if curr.right:
                ans.append(str(curr.right.val))
                queue.append(curr.right)
            else:
                ans.append("X")
        
        return " ".join(ans)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:  return None
        
        data = data.split()
        data = [TreeNode(int(i)) if i != "X" else i for i in data]
        i, ch = 0, 1
        while i < len(data):
            while i < len(data) and data[i] == "X":
                i += 1
            
            l, r = ch, ch + 1
            if i < len(data):
                data[i].left = None if l < len(data) and data[l] == "X" else data[l]
                data[i].right = None if r < len(data) and data[r] == "X" else data[r]
                ch += 2
            
            i += 1
            
        return data[0]
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans