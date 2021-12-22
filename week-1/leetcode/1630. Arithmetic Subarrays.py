def checkArithmeticSubarrays(nums, l, r):
    res = []
    for i in range(len(l)):
        count = 0
        temp_nums = nums[l[i] : r[i] + 1]
        temp_nums.sort()
        temp = temp_nums[1] - temp_nums[0]
        for j in range(len(temp_nums)):
            if j != len(temp_nums) - 1:
                count += 1 if temp != temp_nums[j + 1] - temp_nums[j] else 0
        res.append(bool(0) if count != 0 else bool(1))
    return res


print(
    checkArithmeticSubarrays(
        [7, -6, -3, 0, 0, 0, 0, -8, 2, 16, 8, 12, 4, -5],
        [9, 9, 3, 5, 1],
        [12, 12, 6, 6, 4],
    )
)
