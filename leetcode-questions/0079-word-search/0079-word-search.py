class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        inBounds = lambda row, col: 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def traverseBoard(i, j, index):
            if index == len(word):
                return True
            
            for x, y in DIRS:
                new_i, new_j = i + x, j + y
                if inBounds(new_i, new_j) and word[index] == board[new_i][new_j]:
                    curr_char = board[new_i][new_j]
                    board[new_i][new_j] = 0
                    if traverseBoard(new_i, new_j, index + 1):  return True
                    board[new_i][new_j] = curr_char
                    
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                curr_char = board[i][j]
                if curr_char == word[0]:
                    board[i][j] = 0
                    if traverseBoard(i, j, 1):  return True
                    board[i][j] = curr_char
        
        return False