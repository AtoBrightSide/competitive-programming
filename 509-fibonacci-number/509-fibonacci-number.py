class Solution:
    def fib(self, n: int) -> int:
        @lru_cache
        def dp(n):
            if n == 0 or n == 1:    return n

            curr = dp(n-1) + dp(n-2)

            return curr
        
        return dp(n)