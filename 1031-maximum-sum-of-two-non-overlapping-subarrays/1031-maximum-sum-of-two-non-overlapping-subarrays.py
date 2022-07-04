class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefixSums = [num for num in nums]
        for i in range(1, len(prefixSums)):
            prefixSums[i] = prefixSums[i-1] + nums[i]
        
        def myHelper(win1, win2):
            res = 0
            for i in range(len(nums)):
                if (i+win1) <= len(nums):
                    curr = prefixSums[i+win1-1] - (prefixSums[i-1] if i > 0 else 0)
                    biggest = 0
                    for j in range(len(nums)):
                        if j+win2 <= len(nums) and (j >= win1 + i or win2+j < i):
                            biggest = max(biggest, prefixSums[j+win2-1] - (prefixSums[j-1] if j > 0 else 0))
                    res = max(res, curr + biggest)
                
            return res
        
        
        return max(myHelper(firstLen, secondLen), myHelper(secondLen, firstLen))