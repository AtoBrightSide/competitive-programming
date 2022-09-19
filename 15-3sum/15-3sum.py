class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = set()
        done = set()
        def twoSum(target, i):
            if target in done:  return
            
            done.add(target)
            temp = defaultdict(int)
            for j, num in enumerate(nums):
                if j != i:  
                    temp[num] += 1

            for num in temp:
                curr = target - num
                if curr in temp:
                    potential_triplet = tuple(sorted([-target, num, curr]))
                    if temp[curr] > 1 and curr == num:
                        triplets.add(potential_triplet)
                    if curr != num:
                        triplets.add(potential_triplet)
            
        for i in range(len(nums)):      
            twoSum(-nums[i], i)
        
        
        return list(triplets)