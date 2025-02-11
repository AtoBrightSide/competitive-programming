class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        nums = set()
        l, r = 0, k
        
        while r <= len(s):
            nums.add(s[l:r])
            l += 1
            r += 1
        
        return len(nums) == pow(2, k)