class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        
        for i in range(len(nums)-2):
            l, r = i+1, len(nums) - 1
            while l < r:
                possible_triplet = [nums[i], nums[l], nums[r]]
                
                if sum(possible_triplet) > 0:
                    r -= 1
                elif sum(possible_triplet) < 0:
                    l += 1
                else:
                    triplets.add(tuple(possible_triplet))
                    
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
        
        return triplets