class Solution:
    def largestOddNumber(self, num: str) -> str:
        # start from the end of string, return if odd number present
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2:
                return num[:i + 1]
        
        # if odd number does not exist, return empty list
        return ""