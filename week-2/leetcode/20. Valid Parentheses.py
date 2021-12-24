def isValid(s):
    # create a res variable to store temp parenthesis
    res = []
    # create a dictionary to store opening and closing pairs
    pairs = {"(": ")", "{": "}", "[": "]"}
    # set opening and closing pairs to variables
    openings, closings = "([{", ")]}"
    # now iterate through loop while appending openings to res
    for i in range(len(s)):
        # add all the opening parentheses to the res variable
        if s[i] in openings:
            res.append(s[i])
        # check if the closing parentheses matches the last opening parentheses from res and pop
        elif s[i] in closings and len(res) != 0:
            if pairs[res[-1]] == s[i]:
                res.pop()
            else:
                return False
        else:
            return False
    # if all opening and closing pairs match, then they will be popped, hence s is valid
    return True if len(res) == 0 else False


print(isValid("({()}())"))
