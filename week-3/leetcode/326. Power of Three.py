class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return self.recur(n)

    def recur(self, n):
        if n == 1:
            return True
        elif n < 1:
            return False
        return self.recur(n / 3)
