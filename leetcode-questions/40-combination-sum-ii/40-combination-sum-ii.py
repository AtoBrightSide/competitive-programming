class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combs = set()
        def backtrack(i, so_far, comb):
            if so_far == target:
                combs.add(tuple(comb.copy()))
                return
            
            for curr in range(i, len(candidates)):
                if curr > i and candidates[curr] == candidates[curr - 1]:
                    continue
                if so_far + candidates[curr] <= target:
                    comb.append(candidates[curr])
                    backtrack(curr + 1, candidates[curr] + so_far, comb)
                    comb.pop()
                else:
                    break
        
        backtrack(0, 0, [])
        return combs