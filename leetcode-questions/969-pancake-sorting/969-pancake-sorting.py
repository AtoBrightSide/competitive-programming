class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def maxFinder(end):
            maxNum = 0
            for i in range(end):
                if arr[i] > arr[maxNum]:    maxNum = i
            return maxNum
        
        sorted_arr = sorted(arr)
        L = len(arr)
        end, flips = L, []
        
        while sorted_arr != arr:
            curr_max = maxFinder(end)
            
            if curr_max == 0:
                temp = arr[:end]
                temp = temp[::-1]
                arr = temp + arr[end:]
                flips.append(end)
                end -= 1
                continue
            
            flips.append(curr_max + 1)
            temp = arr[:curr_max+1]
            temp = temp[::-1]
            arr = temp + arr[curr_max+1:]
            
            temp = arr[:end]
            temp = temp[::-1]
            arr = temp + arr[end:]
            flips.append(end)
            
            end -= 1
            
        return flips