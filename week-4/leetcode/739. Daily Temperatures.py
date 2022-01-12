class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create a res variable of length equal to number of temperatures and initialize with 0
        res = [0]*len(temperatures)
        # create a stack to store the indices of the temperatures for comparison
        # append the index of the first temperature to the stack to use as comparator
        mystack=[0]
        # iterate through the temps
        for i in range(1, len(temperatures)):
            # store the index of the current temperature if its less than the temp at the top
            while temperatures[i]>temperatures[mystack[-1]]:
                # append the difference of the current temp and the one on the top of stack to res
                res[mystack[-1]] = i-mystack[-1]
                # pop the index of the previous temperatures
                mystack.pop()
                # if there comes a time when all the indices have been popped, break from the loop
                if mystack == []:
                    break
            # push the next temperature's index to the stack 
            mystack.append(i)
        return res