class Solution:
    def reverseParentheses(self, s: str) -> str:
        # stack to store popped elements
        mystack=[]
        # iterate through the loop for appending elems
        for i in range(len(s)):
            # check if current char is the closing bracket
            if s[i] == ')':
                # return backwards until you get the matching bracket
                temp=[]
                while mystack[-1] != '(':
                    # reverse the string and store in temp
                    temp.append(mystack.pop())
                # pop the matching opening bracket
                mystack.pop()
                # push the reversed sub string to the stack
                mystack.extend(temp)
            else:
                # if the char is not a closing bracketpush to stack
                mystack.append(s[i])
        return "".join(mystack)
