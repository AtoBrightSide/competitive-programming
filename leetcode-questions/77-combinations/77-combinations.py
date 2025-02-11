class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        def backtrack(i, comb):
            if len(comb) == k:
                combs.append(comb.copy())
                return
            
            for curr in range(i+1, n+1):
                comb.append(curr)
                backtrack(curr, comb)
                comb.pop()
                
                
        backtrack(0, [])
        return combs