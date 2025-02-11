class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        queue = deque([n for n in range(len(s) + 1)])
        match = []
        for ch in s:
            if ch == "D":
                curr = queue.pop()
                match.append(curr)
            else:
                curr = queue.popleft()
                match.append(curr)
        if queue:   match.append(queue.pop())
        return match