class Solution:
    def __init__(self):
        self.happy_strings = []
        self.N = 0

    def dfs(self, stack):
        if len(stack) == self.N:
            self.happy_strings.append("".join(stack))
            return

        for letter in "abc":
            if letter != stack[-1]:
                stack.append(letter)
                self.dfs(stack)
                stack.pop()

    def getHappyString(self, n: int, k: int) -> str:
        self.N = n
        for letter in "abc":
            self.dfs([letter])

        self.happy_strings.sort()
        return "" if k > len(self.happy_strings) else self.happy_strings[k - 1]
