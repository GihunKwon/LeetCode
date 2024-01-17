class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = []
        answer = []
        for i,row in enumerate(mat):
            soldiers.append([mat[i].count(1),i])
        for j in sorted(soldiers):
            answer.append(j[1])
            if len(answer) == k:
                break
        return answer