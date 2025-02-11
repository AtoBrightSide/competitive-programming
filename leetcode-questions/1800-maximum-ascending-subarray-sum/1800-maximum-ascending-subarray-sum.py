class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum = max_sum = 0
        prev_num = -float("inf")
        for num in nums:
            curr_sum = (curr_sum + num) if num > prev_num else num
            
            max_sum = max(max_sum, curr_sum)
            prev_num = num
        
        return max_sum