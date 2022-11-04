class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [0] * n
        for i in range(2, int(n ** 0.5) + 1):
            if nums[i]: continue
            
            for j in range(i * i, n, i):
                nums[j] = 1
        
        return max(0, nums.count(0) - 2)
    
    