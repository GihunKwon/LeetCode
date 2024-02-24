class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        answer = -1
        distance = float('inf')
        for index,i in enumerate(points):
            if i[0] == x or i[1] == y:
                if abs(i[0]-x) + abs(i[1]-y) < distance:
                    distance = abs(i[0]-x) + abs(i[1]-y)
                    answer = index
        return answer