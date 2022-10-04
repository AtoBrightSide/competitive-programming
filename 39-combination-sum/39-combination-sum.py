class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combs = set()
        def backtrack(so_far, comb):
            if so_far == target:
                combs.add(tuple(sorted(comb.copy())))
                return
            
            for candidate in candidates:
                if candidate + so_far <= target:
                    comb.append(candidate)
                    backtrack(candidate + so_far, comb)
                    comb.pop()
        
        backtrack(0, [])
        return combs
        