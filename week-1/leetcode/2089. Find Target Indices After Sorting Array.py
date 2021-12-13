def targetIndices(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] >= nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
    found = [i for i in range(len(nums)) if target == nums[i]]
    return found if target in nums else []


print(targetIndices([1, 2, 5, 2, 3], 2))