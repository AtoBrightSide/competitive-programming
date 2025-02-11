class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}
        
        @cache
        def dp(curr, prev, neighbors):
            if neighbors > target:  return float('inf')
            
            if curr == m:
                return 0 if neighbors == target else float('inf')
            
            else:
                ans = float('inf')
                if houses[curr] == 0:
                    for i in range(n):
                        ans=min(ans,cost[curr][i]+dp(curr+1,i+1, neighbors if prev==i+1 else neighbors+1))
                else:
                    ans=min(ans,dp(curr+1,houses[curr],neighbors if houses[curr]==prev else neighbors+1))
                
                return ans
        
        res = dp(0,0,0)
        
        return res if res != float('inf') else -1 