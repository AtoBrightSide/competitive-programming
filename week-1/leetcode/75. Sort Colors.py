def sortColors(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j + 1] < nums[j]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(sortColors([1]))
