class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # building my sequence
        curr_element = 1
        sequence = [1, 1]
        # 1 1 2 3 5
        while curr_element <= k:
            curr_element = sequence[-1] + sequence[-2]
            sequence.append(curr_element)

        # make my greedy choice
        # if I can use a current element, I'd use it, if not, I would just jump to next element
        number_of_fibb = 0
        while sequence and k > 0:
            last_element = sequence.pop()
            if k - last_element >= 0:
                number_of_fibb += (k // last_element)
                k -= last_element

        return number_of_fibb        