class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degrees = defaultdict(list)
        for i, num in enumerate(nums):
            degrees[num].append(i)
        
        L = len(nums)
        shortest_degree = L
        degree = 1
        for num, indices in degrees.items():
            if len(indices) == degree:
                shortest_degree = min(shortest_degree, abs(indices[-1] - indices[0]) + 1)
            if len(indices) > degree:
                shortest_degree = abs(indices[-1] - indices[0]) + 1
                degree = len(indices)
        
        return shortest_degree