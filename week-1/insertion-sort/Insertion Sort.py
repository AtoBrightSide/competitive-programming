def insertionSort1(n, arr):
    # Write your code here
    stored = arr[len(arr) - 1]
    for i in range(len(arr) - 2, -1, -1):
        if stored > arr[i]:
            arr[i + 1] = stored
            print(*arr)
            break
        else:
            arr[i + 1] = arr[i]
            print(*arr)
        if i == 0:
            arr[i] = stored
            print(*arr)


insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])