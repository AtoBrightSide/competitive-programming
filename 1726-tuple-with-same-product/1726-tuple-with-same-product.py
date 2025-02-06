class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = {}
        tuples = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                counter[product] = counter.get(product, 0) + 1
        
        for key, val in counter.items():
            tuples += ((val * (val - 1)) / 2)
        
        return int(tuples * 8)