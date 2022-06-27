class Solution:
    def decodeString(self, s: str) -> str:
        myStack = []
        for ch in s:
            if ch == "]":
                curr = []
                while myStack[-1] != "[":   curr.append(myStack.pop())    
                myStack.pop()
                k = ""
                while myStack and myStack[-1] in "0123456789":  k += myStack.pop()
                curr *= int(k[::-1])
                while curr: myStack.append(curr.pop())
            else:   myStack.append(ch)
                
        return "".join(myStack)