class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = str(n)
        for exp in range(33):
            num = str(2**exp)
            if len(num) == len(n):
                possible = Counter(num) == Counter(n)
                if possible:
                    return True
        
        return False