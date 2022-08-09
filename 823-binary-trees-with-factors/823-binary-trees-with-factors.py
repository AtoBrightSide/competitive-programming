class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        nums = set(arr)
        MOD = (10 ** 9) + 7
        @cache
        def dp(num):
            total = 1
            
            for curr in arr:
                if num % curr == 0 and (num // curr) in nums:
                    total += dp(curr) * dp(num // curr)
            
            return total % MOD
        
        total = 0
        for num in arr:
            total += dp(num)
        
        return total % MOD