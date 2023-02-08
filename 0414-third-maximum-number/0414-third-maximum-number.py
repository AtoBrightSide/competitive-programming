class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        min_heap = nums[:3]
        heapify(min_heap)
        for i in range(3, len(nums)):
            heappushpop(min_heap, nums[i])
        
        if len(min_heap) == 3:
            print("here")
            return heappop(min_heap)
        
        return max(min_heap)