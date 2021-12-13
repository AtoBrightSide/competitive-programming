def select(arr, i):
    # code here
    pass


def selectionSort(arr, n):
    #code here
    for i in range(len(arr)):
        if arr[i] >= min(arr[i:]):
            arr[arr[i:].index(min(arr[i:])) +
                i], arr[i] = arr[i], arr[arr[i:].index(min(arr[i:])) + i]
    return arr


selectionSort([4, 1, 3, 9, 7, 2, 6, 11, 0, 1], 10)
