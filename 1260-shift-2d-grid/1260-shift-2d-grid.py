class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col = len(grid)
        row = len(grid[0])
        size = col * row
        k %= size
        
        grid_list = []
        for i in grid:
            for j in i:
                grid_list.append(j)

        grid_list = grid_list[-k:] + grid_list[:-k]
        
        return [grid_list[i:i+row] for i in range(0,size,row)]