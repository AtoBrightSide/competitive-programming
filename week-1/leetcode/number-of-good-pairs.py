def numIdenticalPairs(nums):
    goodPairs = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            goodPairs = goodPairs+(1 if (nums[i]==nums[j] and i<j) else 0)
    return goodPairs

print(numIdenticalPairs([1,2,3,4]))