class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, 1000000
        while l<=r:
            md = l + (r-l)//2
            if self.helper(nums, md)>threshold:
                l = md + 1
            else:
                r = md - 1
                best = md
        
        return best
    
    def helper(self, nums, div):
        ans = 0
        for num in nums:
            ans += math.ceil(num/div)
        return ans
