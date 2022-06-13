class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(i, j):
            if i == len(triangle):  return 0
            
            if (i, j) in memo:      return memo[(i,j)]
            
            first = triangle[i][j] + dp(i+1, j)
            
            second = triangle[i][j] + dp(i+1, j+1)
            
            memo[(i,j)] = min(first, second)
            return memo[(i,j)]
        
        return dp(0,0)