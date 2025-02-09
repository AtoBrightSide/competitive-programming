class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counter = {}
        for i, num in enumerate(nums):
            counter[i - num] = counter.get(i - num, 0) + 1
        
        N = len(nums)
        total_pairs = int((N * (N - 1)) / 2)
        for freq in counter.values():
            if freq > 1:
                all_pairs = int((freq * (freq - 1)) / 2)
                total_pairs -= all_pairs
        
        return total_pairs