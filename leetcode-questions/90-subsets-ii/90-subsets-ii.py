class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        combs = [[]]
        done = set()
        def backtrack(i, comb):
            
            for curr in range(i+1, len(nums)):
                
                comb.append(nums[curr])
                if tuple(sorted(comb)) not in done:    
                    combs.append(comb.copy())
                    done.add(tuple(sorted(comb.copy())))
                backtrack(curr, comb)
                comb.pop()
        
        backtrack(-1, [])
        return list(combs)