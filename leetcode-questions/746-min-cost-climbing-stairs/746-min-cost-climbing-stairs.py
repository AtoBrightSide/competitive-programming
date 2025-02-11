class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dp(curr):
            if curr == len(cost) - 1:  return cost[curr]
            
            one = two = cost[curr]
            if curr < len(cost) - 1:    one = cost[curr] + dp(curr+1)
            if curr < len(cost) - 2:    two = cost[curr] + dp(curr+2)
            
            ans = min(one, two)
            
            return ans
        
        return min(dp(0), dp(1))