class Large(str):
    def __lt__(a,b):
        return a+b<b+a
    
def largestNumber(nums):
    counter=0
    nums=[str(num) for num in nums]
    nums.sort(key= Large, reverse=True)
    res = "".join(nums)
    for num in nums:
        counter += 1 if num=='0' else 0
    return res if counter != len(nums) else '0'
print(largestNumber([0,0,0,0]))