class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        ans, minDiff = [], float("inf")
        for i in range(1, len(arr)):
            curr = arr[i] - arr[i-1]
            if curr == minDiff:
                ans.append([arr[i-1], arr[i]])
            elif 0 < curr < minDiff:
                ans = [[arr[i-1], arr[i]]]
                minDiff = curr
        
        return ans
        