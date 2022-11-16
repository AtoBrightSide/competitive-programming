# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def traverse(self, root):
        if not root:        
            return ""
        
        queue = deque([root])
        ans = [str(root.val)]
        while queue:
            curr = queue.popleft()
            
            ans.append("X" if not curr.left else str(curr.left.val))
            ans.append("X" if not curr.right else str(curr.right.val))
            
            if curr.left:   
                queue.append(curr.left)
            if curr.right:  
                queue.append(curr.right)
        
        return " ".join(ans)
        
    def serialize(self, root):
        return self.traverse(root)
    
    def deserialize(self, data):
        if len(data) == 0:      
            return None
        data = data.split()
        data = [TreeNode(int(ch)) if ch != "X" else ch for ch in data]
        i = 0
        children = i + 1
        while i < len(data):
            while i < len(data) and data[i] == "X":     i += 1
            
            if i < len(data):   
                node = data[i]
            
            l, r = children, children + 1
            
            node.left = None if l >= len(data) or data[l] == "X" else data[l]
            node.right = None if r >= len(data) or data[r] == "X" else data[r]
            
            children += 2
            i += 1   
        
        return data[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))