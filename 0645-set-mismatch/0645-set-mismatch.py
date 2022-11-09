class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [k for k, val in Counter(nums).items() if val == 2] + [int((len(nums) * (len(nums) + 1))/2) - sum(set(nums))]