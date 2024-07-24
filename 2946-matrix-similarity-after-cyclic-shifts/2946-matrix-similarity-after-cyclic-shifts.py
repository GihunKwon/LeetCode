class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])
        for i in mat:
            if i != i[k:] + i[:k]:
                return False
        return True