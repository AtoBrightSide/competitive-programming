class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        L = len(costs)
        @cache
        def recur(a, b, i):
            if i >= len(costs):
                return 0
            
            goToA = goToB = float("inf")
            if a < L / 2:
                goToA = costs[i][0] + recur(a + 1, b, i + 1)
            if b < L / 2:
                goToB = costs[i][1] + recur(a, b + 1, i + 1)
            
            return min(goToA, goToB)
        
        return recur(0, 0, 0)