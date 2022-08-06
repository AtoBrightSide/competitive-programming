class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie

        def go(pigs, rounds):
            if rounds == 1:
                return 2 ** pigs
            if pigs == 0:
                return 1
            
            # how many buckets can we support
            total = 0
            for p in range(pigs + 1):
                total += comb(pigs, p) * go(pigs - p, rounds - 1)
            return total
                
        for i in range(20):
            if go(i, rounds) >= buckets:    return i
        return 20
            
