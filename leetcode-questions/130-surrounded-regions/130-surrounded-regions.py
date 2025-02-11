class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        isValid = lambda i,j: 0 <= i < len(board) and 0 <= j < len(board[0])
        isEdge = lambda i,j: i == 0 or i == len(board) -1 or j == 0 or j == len(board[i]) - 1
        
        DIRS = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        
        def dp(i, j):
            if (i, j) not in visited:
                visited.add((i,j))
                for d in DIRS:
                    x, y = d[0] + i, d[1] + j
                    if isValid(x, y) and board[x][y] == "O":    dp(x,y)
                        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if isEdge(i, j) and board[i][j] == "O": dp(i, j)
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i,j) in visited:    continue
                board[i][j] = "X"                