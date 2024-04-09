class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        len_mat = [j for i in mat for j in i]
        if len(len_mat) != (r*c):
            return mat
        else:
            new_mat = [] 
            row = []
            for i in len_mat:
                if len(row) < c:
                    row.append(i)
                elif len(row) == c:
                    new_mat.append(row)
                    row = [i]
            if row: 
                new_mat.append(row)
            return new_mat