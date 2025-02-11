class Solution:
    def calculate(self, s: str) -> int:
        s = [ch for ch in s if ch != " "]
        nums = "0123456789"
        i = 0
        ans = []
        while i < len(s):
            curr = ""
            while i < len(s) and s[i] in nums:
                curr += s[i]
                i += 1
            ans.append(curr)
            if i < len(s):  ans.append(s[i])
            i += 1
        s = ans
        def helper(num1, num2, op):
            if op == "/":   return (-1*(abs(num1) // abs(num2))) if num1 * num2 < 0 else num1 // num2
            if op == "*":   return (-1*(abs(num1) * abs(num2))) if num1 * num2 < 0 else num1 * num2
            if op == "+":   return num1 + num2
            if op == "-":   return num1 - num2
            
        stack, i = [int(s[0])], 1
        while i < len(s):
            if s[i] in "*/":
                stack.append(helper(stack.pop(), int(s[i+1]), s[i]))
                i += 1
            if i < len(s) and s[i] in "+-":
                stack.append(int(s[i+1]) if s[i] == "+" else -int(s[i+1]))
            
            i += 1
        
        return sum(stack)
    