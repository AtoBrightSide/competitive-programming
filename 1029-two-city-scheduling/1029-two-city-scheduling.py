class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        cost_diff = sorted([[costs[i][1] - costs[i][0], i] for i in range(len(costs))])
        
        for i, curr in enumerate(cost_diff):
            diff, idx = curr
            if i < len(cost_diff) / 2:
                min_cost += costs[idx][1]
            else:
                min_cost += costs[idx][0]
        
        return min_cost