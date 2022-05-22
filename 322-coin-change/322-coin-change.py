class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(is_needed):
            if is_needed == 0:    return 0
            
            if is_needed in memo: return memo[is_needed]
            
            best = amount + 1
            for coin in coins:
                if is_needed - coin >= 0: 
                    best = min(best, 1 + dp(is_needed - coin))
            
            memo[is_needed] = best
            return memo[is_needed]
            
        for num in range(amount):
            dp(num)
            
        
        ans = dp(amount)
        return ans if ans != amount + 1 else -1