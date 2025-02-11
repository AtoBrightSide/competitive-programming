class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, k - 1
        curr_window = []
        
        for i in range(left, k):
            heappush(curr_window, [-nums[i], i])
        
        max_sliding_window = []
        while right < len(nums):
            heappush(curr_window, [-nums[right], right])
            
            while not left <= curr_window[0][1]:
                heappop(curr_window)
            
            max_sliding_window.append(-curr_window[0][0])
            
            right += 1
            left += 1
            
        return max_sliding_window