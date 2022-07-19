class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l, r, maxFruits = 0, -1, 0
        
        while r < len(fruits):
            while r < len(fruits) and len(basket) < 3:
                r += 1
                if r < len(fruits): basket[fruits[r]] += 1
            
            maxFruits = max(maxFruits, r - l)
            if l < len(fruits) and basket[fruits[l]] == 1:   del basket[fruits[l]]
            else:   basket[fruits[l]] -= 1
            l += 1
                
        return maxFruits