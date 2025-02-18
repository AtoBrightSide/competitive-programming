class Solution:
    def __init__(self):
        self.pattern = ""
        self.smallest = "inf"
        self.conditionTrue = lambda ch, prev, next: (ch == "I" and (prev < next)) or (
            ch == "D" and (prev > next)
        )

    def dfs(self, seen, index, stack):
        if index == len(self.pattern):
            self.smallest = min(self.smallest, "".join(stack))
            return

        for num in "123456789":
            conditionTrue = (
                self.conditionTrue(self.pattern[index], stack[-1], num)
                and num not in seen
            )
            if conditionTrue:
                stack.append(num)
                seen.add(num)
                self.dfs(seen, index + 1, stack)
                seen.remove(num)
                stack.pop()

    def smallestNumber(self, pattern: str) -> str:
        self.pattern = pattern
        for num in "123456789":
            self.dfs(set([num]), 0, [num])

        return self.smallest
