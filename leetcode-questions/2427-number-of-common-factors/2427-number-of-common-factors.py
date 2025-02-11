class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        num = 0
        i = 1
        if a == b:
            while i < a // 2:
                if a % i == 0:  num += 1
                i += 1
        if a > b:
            while i <= b:
                if b % i == 0 and a % i == 0:
                    num += 1
                i += 1
        else:
            while i <= b:
                if b % i == 0 and a % i == 0:
                    num += 1
                i += 1
        return num