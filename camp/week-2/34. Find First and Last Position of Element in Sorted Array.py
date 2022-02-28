class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        return [self.myHelper(nums, target, flag=True), self.myHelper(nums, target, flag=False)]
                
    def myHelper(self, nums, target, flag):
        l,r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]>target:
                r = m - 1
            elif nums[m]<target:
                l = m + 1
            else:
                r = (m-1) if flag else r
                l = l if flag else (m+1)
                best = m
        return best
