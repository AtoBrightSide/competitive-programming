class Solution:     
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []    
                    
        pos_diag = set()
        neg_diag = set()
        cols = set()
                    
        board = [["." for i in range(n)] for j in range(n)]
                    
        def backtrack(i):
            copy = board.copy()
            if i == n:
                curr = []
                for row in copy:
                    curr.append("".join(row))
                res.append(curr)
                return
            for j in range(n):
                if (i+j) not in pos_diag and (i-j) not in neg_diag and j not in cols:
                    pos_diag.add(i+j)
                    neg_diag.add(i-j)
                    cols.add(j)
                    
                    board[i][j] = "Q"
                    backtrack(i+1)
                    board[i][j] = "."
                    
                    pos_diag.remove(i+j)
                    neg_diag.remove(i-j)
                    cols.remove(j)
                    
        
        backtrack(0)
        
        return res
            