class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        answer = [0,0]
        for i in range(len(grid)):
            win = grid[i].count(1)
            if answer[0] < win:
                answer[0] = win
                answer[1] = i
        return answer[1]