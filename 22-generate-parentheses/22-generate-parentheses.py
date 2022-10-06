class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(comb, op, cl):
            if len(comb) == 2 * n:
                res.append("".join(comb))
                return
            
            if op:
                comb.append("(")
                backtrack(comb, op - 1, cl)
                comb.pop()
            if cl > op:
                comb.append(")")
                backtrack(comb, op, cl - 1)
                comb.pop()
        
        backtrack([], n, n)
        return res
        