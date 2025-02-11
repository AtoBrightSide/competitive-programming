class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = str(1 + int("".join([str(x) for x in digits])))
        return [int(x) for x in num]