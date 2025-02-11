class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch.isdigit() and stack:
                stack.pop()
            elif not ch.isdigit():
                stack.append(ch)
        
        return "".join(stack)
        
