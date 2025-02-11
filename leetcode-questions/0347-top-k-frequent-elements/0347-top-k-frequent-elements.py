class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = sorted(Counter(nums).items(), key=lambda x:x[1])
        
        k_frequent = []
        while k:
            k_frequent.append(counter.pop()[0])
            k -= 1
        
        return k_frequent
        
        