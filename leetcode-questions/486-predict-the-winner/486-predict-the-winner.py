class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dp(left, right, turn):
            if left > right:    return 0
            
            if turn:
                return max(nums[left] + dp(left + 1, right, 1 - turn), nums[right] + dp(left, right - 1, 1 - turn))
            else:
                return min(-nums[left] + dp(left + 1, right, 1 - turn), -nums[right] + dp(left, right - 1, 1 - turn))
            
        
        return dp(0, len(nums) - 1, 1) >= 0