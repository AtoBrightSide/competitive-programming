class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        
        for num in nums:
            if num < 0: neg.append(num)
            if num > 0: pos.append(num)

        ans = [] * len(nums)
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        
        return ans