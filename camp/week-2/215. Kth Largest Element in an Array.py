class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(rever)
        retun
        arr = []
        for i in range(len(nums)):
            if i<k:
                heapq.heappush(arr, nums[i])
            else:
                heapq.heappushpop(arr, nums[i])
        return arr[0]
