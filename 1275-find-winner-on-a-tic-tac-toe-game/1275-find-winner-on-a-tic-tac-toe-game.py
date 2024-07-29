class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [["","",""] for _ in range(3)]
        for i,(x,y) in enumerate(moves):
            if i % 2 == 0:
                grid[x][y] = 'A'
            else:
                grid[x][y] = 'B'
        
        for i in range(3):
            # row
            if grid[i][0] == grid[i][1] == grid[i][2] != '':
                return grid[i][0]
            # col
            elif grid[0][i] == grid[1][i] == grid[2][i] != '':
                return grid[0][i]
            # dia 1
            elif i == 0 and grid[i][i] == grid[i+1][i+1] == grid[i+2][i+2] != '':
                return grid[i][i]
            # dia 2
            elif i == 2 and grid[i][0] == grid[i-1][i-1] == grid[0][i] != '':
                return grid[i][0]
        
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'