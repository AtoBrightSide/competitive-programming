class Solution:
    def myPow(self, x: float, n: int):
        if n>=0:
            return self.recur(x, n)
        else:
            return 1/self.recur(x,abs(n))
    def recur(self, num, exp):
        if exp == 0:
            return 1
        temp = self.recur(num,exp//2)
        if exp%2!=0:
            return temp*temp*num
        else:
            return temp*temp

s = Solution()
print(s.myPow(3,3))