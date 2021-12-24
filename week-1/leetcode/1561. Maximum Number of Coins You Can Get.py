def maxCoins(piles):
    # sort the given list
    piles.sort()
    # create res variable to store the coins
    res = 0
    # iterate through the list
    myLen = len(piles) / 3
    for i in range(len(piles)):
        # check the current iteration to not get index out of bounds
        if i < myLen:
            # pop the largest element
            piles.pop()
            # pop the second largest element and store it in res
            res += piles.pop()
        else:
            return res
    return res


print(maxCoins([2, 4, 1, 2, 7, 8]))
