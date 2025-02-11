class Solution:
    def checkEquality(self, stack, part, N):
        return "".join(stack[len(stack) - N:]) == part

    def removeOccurrences(self, s: str, part: str) -> str:
        N = len(part)
        if N > len(s):
            return s

        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= N and self.checkEquality(stack, part, N):
                for _ in range(N):
                    stack.pop()

        return "".join(stack)
