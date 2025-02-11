class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        myStack = []
        curMin = nums[0]
        for i in range(1, len(nums)):
            while myStack and nums[i] > myStack[-1][0]:
                myStack.pop()    
                
            if myStack and myStack[-1][1] < nums[i] < myStack[-1][0]:
                return True
            
            myStack.append((nums[i], curMin))
            curMin = min(curMin, nums[i])
        return False