class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # count how many 0s and 1s there are in each row and column
        # if there is more than 1 one in a row or a col, there is no special pos in that row or col
        rows = len(mat)
        cols = len(mat[0])
        row_count = []
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                count += (1 if mat[i][j] else 0)
            row_count.append(count)
        
        col_count = []
        for j in range(len(mat[0])):
            count = 0
            for i in range(len(mat)):
                count += (1 if mat[i][j] else 0)
            col_count.append(count)
            
        specials = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    specials += 1 if (row_count[i] == 1 and col_count[j] == 1) else 0
        
        return specials