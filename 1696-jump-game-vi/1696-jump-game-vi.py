class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = deque([len(nums)-1])
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if queue[0] - i > k:    queue.popleft() 
            dp[i] = nums[i] + dp[queue[0]]
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            queue.append(i)
        
        return dp[0]