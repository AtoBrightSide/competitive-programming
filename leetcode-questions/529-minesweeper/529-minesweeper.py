class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        isValid = lambda i,j: 0 <= i < len(board) and 0 <= j < len(board[0])
        
        DIRS = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
        
        def dfs(i, j):
            if isValid(i, j) and board[i][j] != "B":
                if board[i][j] == "M":
                    board[i][j] = "X"
                    return
                
                count = 0
                for d in DIRS:
                    x, y = d[0] + i, d[1] + j
                    if isValid(x, y) and board[x][y] == "M":    count += 1
                
                if count == 0:
                    board[i][j] = "B"
                    for d in DIRS:
                        x, y = d[0] + i, d[1] + j
                        dfs(x, y)
                else:
                    board[i][j] = str(count)
                        
        dfs(click[0], click[1])
        
        return board