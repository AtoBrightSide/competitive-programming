class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def maxRobbery(index, robbed, firstPicked):
            if index >= len(nums):
                return 0
            if index == len(nums) - 1 and firstPicked and len(nums) > 1:
                return 0
            pick = dontPick = 0
            if robbed:
                dontPick = maxRobbery(index + 1, False, firstPicked)
            else:    
                pick = max(nums[index] + maxRobbery(index + 1, True, firstPicked), maxRobbery(index + 1, False, firstPicked))
                if index == 0:
                    pick = maxRobbery(index + 1, firstPicked, firstPicked) + (nums[index] if firstPicked else 0)

            return max(pick, dontPick)
        
        return max(maxRobbery(0, False, False), maxRobbery(0, False, True))