def smallerNumbersThanCurrent(nums):
    counter = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            counter[i] = counter[i] + 1 if nums[i] > nums[j] else 0
    print(*counter)


smallerNumbersThanCurrent([6, 5, 4, 8])