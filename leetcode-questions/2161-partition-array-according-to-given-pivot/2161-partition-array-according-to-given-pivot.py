class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower, higher = [], []
        
        for num in nums:
            if num < pivot: lower.append(num)
            if num > pivot: higher.append(num)
                
        for i in range(nums.count(pivot)):
            lower.append(pivot)
        
        for num in higher:
            lower.append(num)
            
        return lower
        