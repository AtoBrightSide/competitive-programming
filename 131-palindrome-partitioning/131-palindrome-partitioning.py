class Solution:
    def partition(self, s: str) -> List[List[str]]:
        isPalindrome = lambda s: s == s[::-1]
        combs = []
        def backtrack(l, comb):
            if l == len(s):
                combs.append(comb.copy())
                return
            
            for r in range(l+1, len(s)+1):
                curr = s[l:r]
                if isPalindrome(curr):
                    comb.append(curr)
                    backtrack(r, comb)
                    comb.pop()
        
        backtrack(0, [])
        return combs