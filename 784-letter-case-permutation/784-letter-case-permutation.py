class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        strings = set([s])
        def backtrack(i, comb):
            if len(comb) == len(s):
                strings.add("".join(comb))
                return 
            
            for j in range(i+1, len(s)):
                curr = s[j]
                # if curr.isdigit():
                #     comb.append(curr)
                #     continue
                comb.append(curr.lower())
                backtrack(j, comb)
                comb.pop()
                
                comb.append(curr.upper())
                backtrack(j, comb)
                comb.pop()
        
        backtrack(-1, [])
        
        return strings