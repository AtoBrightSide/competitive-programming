from collections import Counter


def findOriginalArray(changed):
    res = []
    freq = {}
    changed.sort()
    for num in changed:
        freq[num] = freq.get(num, 0) + 1
    if freq.get(0) and freq.get(0) % 2 != 0:
        return []
    for key in freq:
        while freq[key] > 0:
            if 2 * key in freq and freq[2 * key] > 0:
                res.append(key)
                if freq[2 * key] == 0:
                    continue
                else:
                    freq[2 * key] -= 1
                if freq[key] == 0:
                    continue
                else:
                    freq[key] -= 1
            else:
                return []

    return res


print(findOriginalArray([1, 2, 2, 2, 4, 4]))
