class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        L = len(costs)
        memo = {}
        def recur(a, b, i):
            if i >= len(costs):
                return 0
            if (a, b) not in memo:
                goToA = goToB = float("inf")
                if a < L / 2:
                    goToA = costs[i][0] + recur(a + 1, b, i + 1)
                if b < L / 2:
                    goToB = costs[i][1] + recur(a, b + 1, i + 1)
                
                memo[(a, b)] = min(goToA, goToB)
            
            return memo[(a, b)]
        
        return recur(0, 0, 0)