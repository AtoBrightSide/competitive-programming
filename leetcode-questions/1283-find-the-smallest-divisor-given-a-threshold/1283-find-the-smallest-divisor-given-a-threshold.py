class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        best = 0
        while l <= r:
            md = l + (r - l) // 2
            
            curr = sum([ceil(num/md) for num in nums])

            if curr <= threshold:
                best = md
                r = md - 1
            else:
                l = md + 1
        
        return best