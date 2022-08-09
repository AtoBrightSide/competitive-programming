class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def dp(left, right, turn):
            if left > right:
                return 0
            
            if turn:    
                return max(piles[left] + dp(left + 1, right, 1 - turn), piles[right] + dp(left, right - 1, 1 - turn))
            else:
                return min(-piles[left] + dp(left + 1, right, 1 - turn), -piles[right] + dp(left, right - 1, 1 - turn))
            
        return dp(0, len(piles) - 1, 1) > 0