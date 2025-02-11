class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        counter = sorted(counter.items(), key=lambda x:x[1])
        
        removed, L = 0, len(arr)
        while L > len(arr) / 2:
            L -= counter.pop()[1]
            removed += 1
        
        return removed