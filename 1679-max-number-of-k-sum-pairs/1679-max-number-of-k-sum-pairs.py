class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        freq = Counter(nums)
        for num in nums:
            temp = k-num
            if temp==num and freq[temp]>=2:
                count+=1
                freq[temp]-=2
            elif temp != num and freq[temp]>0 and freq[num]>0:
                count+=1
                freq[temp]-=1
                freq[num]-=1
                
        return count