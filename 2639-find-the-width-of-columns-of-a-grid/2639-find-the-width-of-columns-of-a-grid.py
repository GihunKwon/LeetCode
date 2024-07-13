class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        answer = []
        for i in zip(*grid):
            cnt = 0
            for j in i:
                j = str(j)
                cnt = max(cnt,len(j))
            answer.append(cnt)
        return answer