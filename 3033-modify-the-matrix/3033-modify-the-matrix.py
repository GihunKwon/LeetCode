class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        trans_matrix = []
        for i in zip(*matrix):
            trans_matrix.append(i)
    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = max(trans_matrix[j])
        return matrix