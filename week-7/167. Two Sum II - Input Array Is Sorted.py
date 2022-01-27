class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using 2 pointers, as start and end
        s,e=0,len(numbers)-1
        
        for num in numbers:
            if numbers[s] + numbers[e] == target:
                return [s+1,e+1]
            elif numbers[s] + numbers[e] > target:
                e -= 1
            elif numbers[s] + numbers[e] < target:
                s += 1
                