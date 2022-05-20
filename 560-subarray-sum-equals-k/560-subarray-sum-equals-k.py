class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_map = defaultdict(int)
        my_map[0] = 1
        prefixSum = [n for n in nums]
        
        for i in range(1, len(nums)):
            prefixSum[i] += prefixSum[i-1]
        
        count = 0

        for sums in prefixSum:
            curr = sums - k
            if curr in my_map:
                count += my_map[curr]
            
            my_map[sums] += 1
        return count