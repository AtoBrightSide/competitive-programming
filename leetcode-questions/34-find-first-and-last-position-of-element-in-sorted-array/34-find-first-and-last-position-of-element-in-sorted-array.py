class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(flag):
            l, r = 0, len(nums) - 1
            best = -1
            while l <= r:
                md = l + (r-l)//2

                if target == nums[md]:
                    best = md
                    if flag:        r = md - 1
                    if not flag:    l = md + 1

                if target > nums[md]:   l = md + 1
                elif target < nums[md]:   r = md - 1
                
            return best
        
        return [bs(True), bs(False)]