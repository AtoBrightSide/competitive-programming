class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            prev, nxt = i-1, i+1
            if flowerbed[i] == 1:
                continue
            else:
                if len(flowerbed) == 1:
                    n -= 1
                    flowerbed[i] = 1
                elif i == 0 and self.checker(flowerbed, nxt):
                    if flowerbed[nxt] == 0:
                        n -= 1
                        flowerbed[i] = 1
                elif i == len(flowerbed)-1 and self.checker(flowerbed, prev):
                    if flowerbed[prev] == 0:
                        n -= 1
                        flowerbed[i] = 1
                elif self.checker(flowerbed, prev) and self.checker(flowerbed, nxt):
                    if flowerbed[prev] == flowerbed[nxt] == 0:
                        n -= 1
                        flowerbed[i] = 1
            print(n)
        return True if n <= 0 else False
    
    def checker(self, flowerbed, i):
        return 0<=i<len(flowerbed)
