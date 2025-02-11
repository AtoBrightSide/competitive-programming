class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        memo = set()
        
        for i in range(9):
            for j in range(9):
                if f"{board[i][j]} R{i}" in memo or f"{board[i][j]} C{j}" in memo or f"{board[i][j]} B{i//3}{j//3}" in memo:
                    return False
                
                if board[i][j] != '.':
                    memo.add(f"{board[i][j]} R{i}")
                    memo.add(f"{board[i][j]} C{j}")
                    memo.add(f"{board[i][j]} B{i//3}{j//3}")
            
        return True