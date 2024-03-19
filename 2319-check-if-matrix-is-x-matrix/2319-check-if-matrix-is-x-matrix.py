class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        answer = True
        l = len(grid[0])-1
        for i in range(len(grid)):
            if grid[i][i] == 0:
                answer = False
                break
            if grid[l-i][i] == 0:
                answer = False
                break
            for j in range(len(grid[0])):
                if i != j and i+j != l:
                    if grid[i][j] != 0:
                        answer = False
                        break
        return answer