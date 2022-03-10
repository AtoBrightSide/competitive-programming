class Solution:
    def fib(self, n: int) -> int:
        d = {}
        
        return self.dp(n, d)
    def dp(self, n, d):
        if n == 0 or n == 1:
            return n
        if n in d:
            return d[n]
        
        a = self.dp(n-1, d)
        b = self.dp(n-2, d)
        
        d[n] = a + b
        
        return a + b
        
