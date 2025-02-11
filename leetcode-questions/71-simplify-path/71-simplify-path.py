class Solution:
    def simplifyPath(self, path: str) -> str:
        queue = deque(path.split('/')[1:])
        stack = ['/']
        
        while queue:
            curr = queue.popleft()
            if curr == "..":
                if len(stack) > 2:
                    stack.pop()
                    stack.pop()
            elif len(curr) > 0 and curr != '.':
                stack.append(curr)
                stack.append('/')
        
        if len(stack) > 1:    stack.pop()
        
        return "".join(stack)