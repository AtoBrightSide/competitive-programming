class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(comb):
            stack = []
            for ch in comb:
                if ch == "(":
                    stack.append("(")
                else:
                    if not stack:   return False
                    stack.pop()
            return stack == []
        
        res = []
        def backtrack(comb):
            if len(comb) == 2 * n:
                if isValid(comb):   res.append("".join(comb))
                return
            
            comb.append("(")
            backtrack(comb)
            comb.pop()
            
            comb.append(")")
            backtrack(comb)
            comb.pop()
        
        backtrack([])
        return res
        