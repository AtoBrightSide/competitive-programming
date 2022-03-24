class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s = {}
        one = self.dp(cost, 0, s)
        
        two = self.dp(cost, 1, s)
        
        return min(one, two)
        
    def dp(self, cost, i, vis):
        if not i < len(cost):
            return 0
            
        if i in vis:
            return vis[i]
        
        one = self.dp(cost, i+1, vis)
        
        two = self.dp(cost, i+2, vis)
        
        res = min(one,two) + cost[i]
        
        vis[i] = res
        
        return res
