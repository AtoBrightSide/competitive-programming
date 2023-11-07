class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # append difference in cost between two cities, and sort based on that
        costs = sorted([[a, b, abs(a - b)] for a, b in costs], key=lambda cost: cost[2], reverse=True)
        # prioritize the costs with biggest differences, while cities are not full.
        min_cost = 0
        a_count = b_count = 0
        n = len(costs)
        for a_cost, b_cost, cost_diff in costs:
            if a_cost <= b_cost:
                if a_count < n / 2:
                    min_cost += a_cost
                    a_count += 1
                else:
                    min_cost += b_cost
                    b_count += 1
            else:
                if b_count < n / 2:
                    min_cost += b_cost
                    b_count += 1
                else:
                    min_cost += a_cost
                    a_count += 1
        
        return min_cost