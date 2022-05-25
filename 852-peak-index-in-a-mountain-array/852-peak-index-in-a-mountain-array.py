class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        
        while l <= r:
            md = l + (r - l) // 2
            
            if arr[md - 1] < arr[md] > arr[md + 1]:
                return md
            if arr[md] > arr[md - 1]:
                l = md
            else:
                r = md