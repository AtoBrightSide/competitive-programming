from collections import Counter


def minSetSize(arr):
    # create res variable to store the frequency of the numbers
    res = 0
    # count the freq of each element
    freq = Counter(arr)
    # initialize a counter
    counter = 0
    # store the occurence of each element in a separate list
    occurence = list(freq.values())
    # sort the list of occurences in such a way to get the most frequent element first
    occurence.sort(reverse=True)
    # iterate through freq
    for oc in occurence:
        # increse counter by one to signify a single number has been used
        counter += 1
        # store the freq of the keys that are being iterated through
        res += oc
        # check to see if there are enough elements to reduce the array to half
        if res >= len(arr) / 2:
            # if so, return counter
            return counter


print(minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
