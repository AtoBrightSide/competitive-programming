class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        
        def dp(i):
            if i >= len(questions) - 1:
                return questions[-1][0] if i == len(questions) - 1 else 0
            
            if i in memo:   return memo[i]
            
            solve = questions[i][0] + dp(i + questions[i][1] + 1)
            
            skip = dp(i + 1)
            
            memo[i] = max(solve, skip)
            
            return memo[i]
        
        ans = dp(0)
        
        return ans