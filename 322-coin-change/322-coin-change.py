class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        memo = {}
        def dfs(remainder):
            if remainder == 0:  return 0
            
            if remainder in memo:   return memo[remainder]
            
            best = float('inf')
            for coin in coins:
                curr = remainder - coin
                if curr >= 0:   best = min(1 + dfs(curr), best)
                    
            memo[remainder] = best
            return memo[remainder]
        
        best = float('inf')
        for coin in coins:
            best = min(best, 1 + dfs(amount - coin))
            
        return -1 if best == float('inf') else best