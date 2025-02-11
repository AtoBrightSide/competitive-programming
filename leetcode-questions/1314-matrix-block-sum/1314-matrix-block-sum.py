class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix_sums = []
        for row in mat:
            curr_row = [row[0]]
            for i in range(1, len(row)):
                elt = row[i]
                curr_row.append(curr_row[-1] + elt)
            prefix_sums.append(curr_row)
        
        answer = []
        for i in range(len(mat)):
            i_l, i_r = max(0, i - k), min(i + k, len(mat) - 1)
            curr_row = []
            for j in range(len(mat[0])):
                j_l, j_r = max(0, j - k), min(j + k, len(mat[0]) - 1)
                curr_elt = 0
                for m in range(i_l, i_r + 1):
                    curr_elt += prefix_sums[m][j_r] - (0 if j_l == 0 else prefix_sums[m][j_l - 1])
                curr_row.append(curr_elt)
            answer.append(curr_row)
        
        return answer