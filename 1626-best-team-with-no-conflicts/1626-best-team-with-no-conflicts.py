class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = sorted([[scores[i], ages[i]] for i in range(len(ages))], key=lambda x:(x[1], x[0]))
        
        @cache
        def dp(i, flag, prev):
            if i >= len(pairs):
                return 0
            
            pick = dont_pick = 0
            if i == 0 or flag or pairs[i][0] >= pairs[prev][0]:
                pick = pairs[i][0] + dp(i + 1, False, i)
            
            dont_pick = dp(i + 1, False, prev)
            
            return max(pick, dont_pick)
        
        best_score = 0
        for i in range(len(pairs)):
            best_score = max(best_score, dp(i, True, 0))
        
        return best_score