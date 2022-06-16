class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue, visited = deque([start]), set()
        isValid = lambda i: 0 <= i < len(arr)

        while queue:
            curr = queue.popleft()
            visited.add(curr)
            
            front = curr + arr[curr]
            back = curr - arr[curr]
            
            if (isValid(front) and arr[front] == 0) or (isValid(back) and arr[back] == 0):
                return True
            
            if isValid(front) and front not in visited:     queue.append(front)
            if isValid(back) and back not in visited:       queue.append(back)
            
        return False