def countingSort(arr):
    # Write your code here
    counter = [0] * (1 + max(arr))
    for num in arr:
        counter[num] += 1

    return counter