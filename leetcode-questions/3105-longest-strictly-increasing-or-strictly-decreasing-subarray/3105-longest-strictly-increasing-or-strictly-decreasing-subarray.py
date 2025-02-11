class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best = 1
        stack = [-float('inf')]
        for num in nums:
            if num > stack[-1]: 
                stack.push(num)
            best = max(best, len(stack))
        
        prev = float('inf')
        decreasingCount = 0
        for num in nums:
            decreasingCount = (decreasingCount + 1) if num < prev else 1
            best = max(best, decreasingCount)
            prev = num
        
        return best
