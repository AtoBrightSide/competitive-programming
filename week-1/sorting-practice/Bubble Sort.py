def countSwaps(a):
    # Write your code here
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    print(
        f"Array is sorted in {swaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[len(a)-1]}"
    )


countSwaps([3, 4, 1, 2, 5])