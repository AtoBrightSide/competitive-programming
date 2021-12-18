def kthLargestNumber(nums, k):
    nums.sort(key=lambda x:int(x))
    return nums[k-1]
kthLargestNumber(["2","21","12","1","210","20"], 3)