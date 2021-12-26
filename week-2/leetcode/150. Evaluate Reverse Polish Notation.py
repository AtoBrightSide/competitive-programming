def evalRPN(tokens):
    # store all operations in ops variable
    ops = "+/*-"
    # declare list to store numbers
    nums = []
    # iterate through the loop
    for char in tokens:
        # if char is an operation,
        if char in ops:
            # assign two of the last elements to temp variables for calculation
            temp1, temp2 = nums.pop(), nums.pop()
            # then apply operation on temp1, temp2 and push result to nums
            if char == "+":
                nums.append(temp1 + temp2)
            elif char == "-":
                nums.append(temp2 - temp1)
            elif char == "*":
                nums.append(temp1 * temp2)
            else:
                nums.append(
                    int(temp2 / temp1)
                    if (temp1 < 0 or temp2 < 0)
                    else int(temp2 // temp1)
                )
        else:
            # push the numbers to the nums
            nums.append(int(char))
    return nums[0]


evalRPN(["2", "1", "+", "3", "*"])
