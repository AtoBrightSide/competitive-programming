def movezeroes(nums):
    temp = [0] * len(nums)
    c=0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp[c] = nums[i]
            c+=1
    print(temp)
(movezeroes(nums=[0,1,0]))