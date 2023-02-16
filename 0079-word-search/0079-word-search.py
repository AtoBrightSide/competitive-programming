class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [[0, 1], [1, 0], [0,-1], [-1, 0]]
        inBounds = lambda i, j: 0 <= i < len(board) and 0 <= j < len(board[0])
        L = len(word)
        
        def backtrack(i, j, count):
            if count == L:
                return True

            for x, y in DIRS:
                new_i, new_j = x + i, y + j
                if inBounds(new_i, new_j) and board[new_i][new_j] == word[count]:
                    board[new_i][new_j] = -1
                    if backtrack(new_i, new_j, count + 1):
                        return True
                    board[new_i][new_j] = word[count]

            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = -1
                    if backtrack(i, j, 1):
                        return True
                    board[i][j] = word[0]
        
        return False