class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        strings = set()
        def backtrack(i, comb):
            if len(comb) == len(s):
                strings.add("".join(comb))
                return 
            
            curr = s[i]
            if not curr.isdigit():  backtrack(i+1, comb + list(curr.swapcase()))
            backtrack(i+1, comb + list(curr))
                
        backtrack(0, [])
        
        return strings