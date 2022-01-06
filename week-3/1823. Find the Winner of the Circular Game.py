class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # make a list of the numbers
        n = [num + 1 for num in range(n)]
        # call the helper function with the starting index
        return self.recur(n, k, 0)

    def recur(self, n, k, i):
        # variable to get a hold of kth element, initialize to 1
        p = 1
        # iterate through an infinite loop
        while True:
            # base case
            if len(n) == 1:
                return n[0]
            # check if the kth turn has been reached
            if p == k:
                # if so, remove the element at that index
                n.pop(i)
                # check if the index is still within the range of the list, and do it all again
                if i >= len(n):
                    i = 0
                self.recur(n, k, i)
            # increase the counter as well as the turn of the player
            p += 1
            i += 1
            # if it is the last players turn, return to the first player
            if i >= len(n):
                i = 0
