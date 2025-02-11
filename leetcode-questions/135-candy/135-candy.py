class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        
        for i in range(len(ratings) - 1):
            if ratings[i] > ratings[i+1]:   
                candies[i] = (candies[i+1] + 1) if candies[i] <= candies[i+1] else candies[i]
            
            if ratings[i] < ratings[i+1]:   
                candies[i+1] = (candies[i] + 1) if candies[i] >= candies[i+1] else candies[i+1]
        
        ans = 0
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i] if candies[i] > candies[i-1] else (candies[i-1] + 1)
            if ratings[i] < ratings[i-1]:
                candies[i-1] = candies[i-1] if candies[i] < candies[i-1] else (candies[i] + 1)
            ans += candies[i]
                
        return ans + candies[0]