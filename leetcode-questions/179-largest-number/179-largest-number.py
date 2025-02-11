class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        
        ans = []
        counter = Counter(nums)
        
        if counter["0"] == len(nums):   return "0"
        
        while len(ans) < len(nums):
            largest = "0"
            for num in nums:
                if counter[num] == 0:   continue
                largest = largest if int(largest+num) > int(num+largest) else num

            ans.append(largest)
            counter[largest] -= 1
            
        return "".join(ans)