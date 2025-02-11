class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        
        def recur(x, n):
            if n == 0:  return 1
            
            if n % 2 == 0:  return recur((x*x) % MOD, n/2)
            else:  return x * recur((x*x) % MOD, (n-1)/2) % MOD
        
        ans = recur(20, n//2)
        return (ans * (5 if n % 2 != 0 else 1)) % MOD