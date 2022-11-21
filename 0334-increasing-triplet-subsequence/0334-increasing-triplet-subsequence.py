class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = num2 = float("inf")
        for i, num in enumerate(nums):
            if num <= num1:
                num1 = num
            elif num <= num2:
                num2 = num
            elif num > num2:
                return True

        return False