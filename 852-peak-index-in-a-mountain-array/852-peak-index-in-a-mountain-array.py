class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        for i in range(len(arr)):
            if 0 < i < len(arr) - 1 and arr[i-1] < arr[i] > arr[i+1]:
                return i
            
            