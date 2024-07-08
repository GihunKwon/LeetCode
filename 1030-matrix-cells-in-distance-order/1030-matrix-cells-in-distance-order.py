class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        coor = []
        for i in range(rows):
            for j in range(cols):
                coor.append([i,j])
        coor.sort(key=lambda x: abs(x[0]-rCenter) + abs(x[1]-cCenter))

        return coor