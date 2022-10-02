class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSums = [nums[0]]
        for i in range(1, len(nums)):
            prefixSums.append(prefixSums[-1] + nums[i])
        
        remains = defaultdict(list)
        for i, prefix in enumerate(prefixSums):
            curr = prefix % k
            if (curr in remains and remains[curr][0] < i-1) or (curr == 0 and i > 0):
               return True
            remains[curr].append(i)
        
        return False