class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        
        '''
            ,
        - 1 5 6
        
        left -
        right 5
        count 1
        '''
        
        for i in range(len(nums) - 1):
            left, right = i - 1, i + 1
            
            if nums[i] > nums[right]:
                count += 1
                if count > 1:   
                    return False
                if i == 0:   
                    nums[i] = -float('inf')
                elif nums[left] > nums[right]:  
                    nums[right] = nums[i]
                else:
                    nums[i] = nums[left]
                    
        return True