class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer = 0
        l = len(grid[0])
        for i in range(l):
            ans = 0
            for j in grid:
                ans = max(ans,max(j))
                j.remove(max(j))
            answer += ans
        return answer