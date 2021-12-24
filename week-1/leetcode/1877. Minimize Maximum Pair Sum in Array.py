def minPairSum(nums):
    # sort the given list
    nums.sort()
    # create a res variable to store pairs
    res = []
    # store the mid value of the nums
    mid_arr = len(nums) / 2
    # iterate through the loop
    for i in range(len(nums)):
        # check to see if the current iteration is below the mid
        if i < mid_arr:
            # insert a pair of the largest and smallest elements to the res variable
            res.append([nums[i], nums.pop()])
        else:
            break
    # sorting the res list based on the sum of the pairs so that the largest sum is at index 0
    res.sort(key=lambda x: x[0] + x[1], reverse=True)
    # return the sum of the first pair(which is the largest)
    return res[0][0] + res[0][1]


print(minPairSum([3, 5, 2, 3]))
