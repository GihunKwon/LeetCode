class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = [0,0]
        for i,row in enumerate(mat):
            if row.count(1) > answer[1]:
                answer[0] = i
                answer[1] = row.count(1)
        return answer