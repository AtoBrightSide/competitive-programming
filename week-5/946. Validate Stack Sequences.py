class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # create an empty stack
        stack = []
        # create a counter to hold the current iteration of both lists
        c=0
        # iterate through the pushed list 
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[c]:
                stack.pop()
                c += 1
        return stack == []
