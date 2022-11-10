class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num = 0
        for x in nums:
            num ^= x
        
        pos = int(math.log2(num & ~(num - 1)))
        ans = [0, 0]
        
        for x in nums:
            if not x ^ ((1 << pos) | x):
                ans[0] ^= x
        
        ans[1] = ans[0] ^ num
        return ans